from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.payment.models import Payment
from apps.payment.serializers import PaymentSerializer, PaymentFinishSerializer, PaymentRollbackSerializer


class PaymentView(GenericViewSet, CreateModelMixin):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentFinishView(GenericViewSet, UpdateModelMixin):
    queryset = Payment.objects.all()
    serializer_class = PaymentFinishSerializer


class PaymentRollbackView(GenericViewSet, UpdateModelMixin):
    queryset = Payment.objects.all()
    serializer_class = PaymentRollbackSerializer