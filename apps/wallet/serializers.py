from rest_framework import serializers

from apps.wallet.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    """Сериалайзер для кошелька"""
    class Meta:
        model = Wallet
        fields = "__all__"
