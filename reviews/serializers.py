from rest_framework import serializers

from ads.models import Advertisement
from reviews.models import Comment
from users.models import User


class CommentViewSerializer(serializers.ModelSerializer):
    ad_id = serializers.PrimaryKeyRelatedField(queryset=Advertisement.objects.all(),
                                               many=False)
    author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                                   many=False)
    author_first_name = serializers.RelatedField(source='author.first_name', read_only=True)
    author_last_name = serializers.RelatedField(source="author.last_name", read_only=True)
    author_image = serializers.CharField(source="author.image", read_only=True)

    class Meta:
        model = Comment
        fields = ["pk", "text",  "created_at",
                  "author_id", "author_first_name", "author_last_name", "author_image",
                  "ad_id",]

