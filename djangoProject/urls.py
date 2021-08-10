from django.urls import path, include

urlpatterns = [
    path('comments/', include('commentary.urls')),
    path('articles/', include('article.urls')),
]
