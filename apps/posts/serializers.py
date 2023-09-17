from rest_framework import serializers

from apps.categories.serializers import CategorySerializer
from apps.posts.models import Post


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
    category_name = CategorySerializer()

    class Meta:
        model = Post
        fields = ('title', 'short_info', 'category_name', 'created_at')
