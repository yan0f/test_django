from django.urls import path
from .api import ArticleCreateApi

urlpatterns = [
    path('', ArticleCreateApi.as_view()),
]
