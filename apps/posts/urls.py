from rest_framework.routers import DefaultRouter as DR

from apps.posts.views import PostViewSet


router = DR()
router.register('post', PostViewSet, basename='posts')

urlpatterns = [

]

urlpatterns += router.urls
