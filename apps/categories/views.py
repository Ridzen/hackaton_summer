from rest_framework import generics, permissions

from apps.categories.serializers import CategorySerializer


class CategoryView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
