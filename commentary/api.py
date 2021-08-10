from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Commentary
from .serializer import CommentarySerializer


class CommentaryCreateView(CreateAPIView):
    """
    Добавление комментария к статье.
    Добавление коментария в ответ на другой комментарий (возможна любая вложенность).
    """
    # TODO: запретить создавать дочерние комментарии с отличным от родительского article_id
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer


@api_view()
def get_root_and_three_child_comments_for_article(_: Request, article_id: int) -> Response:
    """
    Получение всех комментариев к статье вплоть до 3 уровня вложенности
    """
    commentaries = Commentary.objects \
        .filter(article_id=article_id) \
        .filter(level__lte=3).all()
    serializer = CommentarySerializer(commentaries, many=True)
    return Response(serializer.data)


@api_view()
def get_all_comments_for_comment(_: Request, comment_id: int) -> Response:
    """
    Получение всех вложенных комментариев для комментария 3 уровня
    """
    query = Commentary.objects.filter(parent=comment_id).get_descendants(include_self=True)
    serializer = CommentarySerializer(query, many=True)
    return Response(serializer.data)
