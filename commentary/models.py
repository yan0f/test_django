from django.db import models
from mptt.fields import TreeForeignKey

from article.models import Article
from mptt.models import MPTTModel


class Commentary(MPTTModel):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    content = models.CharField(max_length=1000)
    publish_date = models.DateTimeField()
