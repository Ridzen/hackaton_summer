from django.urls import path

from apps.posts.views import (
    PostListByCategoryViewSet, PostCreateViewSet, PostRetrieveViewSet, CommentCreateView,
    PostUpdateViewSet, PostDestroyViewSet, LikeCreateView, CommentListView
)

urlpatterns = [
    path('posts/<int:category_id>', PostListByCategoryViewSet.as_view({'get': 'list'}), name='post_list_by_category'),
    path('posts/create/', PostCreateViewSet.as_view({'post': 'create'}), name='post_create'),
    path('posts/<int:pk>/', PostRetrieveViewSet.as_view({'get': 'retrieve'}), name='post_retrieve'),
    path('posts/<int:pk>/update/', PostUpdateViewSet.as_view({'patch':'partial_update', 'put': 'update'}), name='post_update'),
    path('posts/<int:pk>/delete/', PostDestroyViewSet.as_view({'delete': 'destroy'}), name='post_delete'),
    path('posts/comment/', CommentCreateView.as_view()),
    path('posts/like/', LikeCreateView.as_view()),
    path('posts/comments/<int:post_id>/', CommentListView.as_view())
]
