from rest_framework import mixins
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin, CreateModelMixin
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import status


class PostMixin(
    mixins.RetrieveModelMixin, mixins.ListModelMixin,
    mixins.UpdateModelMixin, GenericViewSet, CreateModelMixin
):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

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
