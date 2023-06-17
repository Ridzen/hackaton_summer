from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.wallet.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    """Сериалайзер для кошелька"""
    class Meta:
        model = Wallet
        fields = (
            'id', 'owner',
            'rs_number', 'balance'
        )


class WalletUpdateSerializer(serializers.ModelSerializer):
    """Сериалайзер для кошелька"""

    rs_number = serializers.CharField(write_only=True, required=True)
    balance = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = Wallet
        fields = (
            'id', 'rs_number', 'balance'
        )

    def update(self, instance, validated_data):
        rs_number = validated_data.get("rs_number")
        balance = validated_data.get("balance")

        if instance.rs_number == rs_number:
            instance.balance += balance
            instance.save()
        else:
            raise ValidationError({"Value error": "Sorry, but this wrong rs_number"})

        return instance
