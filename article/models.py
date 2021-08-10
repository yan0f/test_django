from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    publish_date = models.DateTimeField()
