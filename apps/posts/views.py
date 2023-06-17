from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    """Post ViewSets"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = permissions.IsAuthenticated
