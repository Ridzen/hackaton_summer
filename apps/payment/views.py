from rest_framework.mixins import (
    CreateModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import (
    IsAuthenticated
)

from apps.payment.models import Payment
from apps.payment.serializers import (
    PaymentSerializer, PaymentFinishSerializer, PaymentRollbackSerializer
)


class PaymentView(GenericViewSet, CreateModelMixin):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = IsAuthenticated


class PaymentFinishView(GenericViewSet, UpdateModelMixin):
    queryset = Payment.objects.all()
    serializer_class = PaymentFinishSerializer
    permission_classes = IsAuthenticated


class PaymentRollbackView(GenericViewSet, UpdateModelMixin):
    queryset = Payment.objects.all()
    serializer_class = PaymentRollbackSerializer
    permission_classes = IsAuthenticated
