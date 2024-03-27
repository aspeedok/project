from rest_framework import serializers
from apps.posts.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "name", "text", "created_at"]
