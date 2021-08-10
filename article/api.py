from rest_framework.generics import CreateAPIView

from .models import Article
from .serializer import ArticleSerializer


class ArticleCreateApi(CreateAPIView):
    """Добавление статьи"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
