from django.urls import path

from .api import CommentaryCreateView, get_root_and_three_child_comments_for_article, get_all_comments_for_comment

urlpatterns = [
    path('', CommentaryCreateView.as_view()),
    path('root/<int:article_id>', get_root_and_three_child_comments_for_article),
    path('all/<int:comment_id>', get_all_comments_for_comment),
]
