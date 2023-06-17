from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.payment.models import Payment
from apps.payment.serializers import PaymentSerializer


class PaymentView(GenericViewSet, CreateModelMixin):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
