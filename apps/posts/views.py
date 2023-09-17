from rest_framework import permissions, generics, status
from rest_framework.response import Response

from apps.auths.models import Profile
from apps.posts.mixins import (
    PostCreateMixin, PostRetrieveMixin, PostUpdateMixin,
    PostListMixin, PostDestroyMixin
)
from apps.posts.models import Post, Comment, Like
from apps.posts.serializers import (
    PostSerializer, PostByCategorySerializer, CommentSerializer, LikeSerializer
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


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)


class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def post(self, request, *args, **kwargs):
        user = self.request.user
        post_id = self.request.data.get('post')
        post = Post.objects.get(pk=post_id)

        try:
            user_profile = Profile.objects.get(user_profile=user)
        except Profile.DoesNotExist:
            return Response(
                {'detail': 'Профиль пользователя не найден'},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            like = Like.objects.get(user=user_profile, post=post)
            like.delete()
            return Response(
                {'detail': 'Лайк успешно убран'}, status=status.HTTP_200_OK
            )
        except Like.DoesNotExist:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user_profile, post=post)
            return Response(
                {'detail': 'Лайк успешно поставлен'}, status=status.HTTP_201_CREATED
            )

