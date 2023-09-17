from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin, CreateModelMixin
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status


class PostCreateMixin(
     GenericViewSet, CreateModelMixin
):
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PostListMixin(
    GenericViewSet, ListModelMixin, RetrieveModelMixin
):
    """
    List a queryset by category.
    """
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return self.queryset.filter(category_id=category_id)


class PostUpdateMixin(
    GenericViewSet, UpdateModelMixin
):
    """
     Update a model instance.
     """
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()


class PostRetrieveMixin(
    GenericViewSet, RetrieveModelMixin
):
    """
    Retrieve a model instance.
    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PostDestroyMixin(
    GenericViewSet, DestroyModelMixin
):
    """
    Destroy a model instance.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
