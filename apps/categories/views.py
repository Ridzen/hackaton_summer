from rest_framework import generics, permissions

from apps.categories.serializers import CategorySerializer


class CategoryView(generics.CreateAPIView):
    permission_classes = permissions.AllowAny
    serializer_class = CategorySerializer
