from rest_framework import serializers

from apps.categories.serializers import CategorySerializer
from apps.posts.models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для постов"""
    class Meta:
        model = Post
        fields = (
            "title", "short_info", "status",
            "full_info", "business_plan_file", "amount", "amount_rest",
            "amount_per_season", "amount_of_person", "category_id",
            "user_profile_id"
        )


class PostByCategorySerializer(serializers.ModelSerializer):
    """Get Post By Category"""

    class Meta:
        model = Post
        fields = ('title', 'short_info', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    """Create Comment"""

    class Meta:
        model = Comment
        fields = (
            'user',
            'post',
            'parent_comment',
            'content',
        )


class LikeSerializer(serializers.ModelSerializer):
    """Likes"""

    class Meta:
        model = Like
        fields = (
            'post',
            'user',
        )
