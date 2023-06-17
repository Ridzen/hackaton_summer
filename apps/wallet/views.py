from rest_framework import permissions
from rest_framework import generics

from apps.wallet.models import Wallet
from apps.wallet.serializers import WalletSerializer, WalletUpdateSerializer


class WalletViewSet(generics.CreateAPIView):
    """Wallet ViewSet"""
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = permissions.AllowAny


class WalletUpdateViewSet(generics.UpdateAPIView):
    """Wallet ViewSet"""
    queryset = Wallet.objects.all()
    serializer_class = WalletUpdateSerializer
    permission_classes = permissions.AllowAny
