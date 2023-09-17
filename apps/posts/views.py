from rest_framework import permissions

from apps.posts.mixins import (
    PostCreateMixin, PostRetrieveMixin, PostUpdateMixin,
    PostListMixin, PostDestroyMixin
)
from apps.posts.models import Post
from apps.posts.serializers import (
    PostSerializer, PostByCategorySerializer
)


class PostListByCategoryViewSet(PostListMixin):
    """List By Category ViewSets"""
    queryset = Post.objects.all()
    serializer_class = PostByCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class PostCreateViewSet(PostCreateMixin):
    """Post ViewSets"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostRetrieveViewSet(PostRetrieveMixin):
    """Retrieve ViewSets"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostUpdateViewSet(PostUpdateMixin):
    """Update ViewSets"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDestroyViewSet(PostDestroyMixin):
    """Destroy ViewSets"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
