from rest_framework.serializers import ModelSerializer

from .models import Commentary


class CommentarySerializer(ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('id', 'parent', 'article_id', 'content', 'publish_date')
