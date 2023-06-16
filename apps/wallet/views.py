from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from apps.wallet.models import Wallet
from apps.wallet.serializers import WalletSerializer


class WalletViewSet(ModelViewSet):
    """Wallet ViewSet"""
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = permissions.IsAuthenticated
