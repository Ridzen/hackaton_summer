from rest_framework import permissions

from apps.posts.mixins import PostMixin
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostViewSet(PostMixin):
    """Post ViewSets"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
