import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.wallet.models import Wallet


def check_expiry_month(value):
    if not 1 <= int(value) <= 12:
        raise serializers.ValidationError("Invalid expiry month.")


def check_expiry_year(value):
    today = datetime.datetime.now()
    if not int(value) >= today.year:
        raise serializers.ValidationError("Invalid expiry year.")


def check_cvc(value):
    if not 3 <= len(value) <= 4:
        raise serializers.ValidationError("Invalid cvc number.")


def check_payment_method(value):
    payment_method = value.lower()
    if payment_method not in ["card"]:
        raise serializers.ValidationError("Invalid payment_method.")


class WalletSerializer(serializers.ModelSerializer):
    """Сериалайзер для кошелька"""

    card_number = serializers.CharField(
        write_only=True, required=True, source='rs_number'
    )
    expiry_month_card = serializers.CharField(
        write_only=True,
        required=True,
        validators=[check_expiry_month],
        source='expiry_month'
    )
    expiry_year_card = serializers.CharField(
        write_only=True,
        required=True,
        validators=[check_expiry_year],
        source='expiry_year'
    )
    cvc_card = serializers.CharField(
        write_only=True,
        required=True,
        validators=[check_cvc],
        source='cvc'
    )

    class Meta:
        model = Wallet
        fields = ('card_number', 'balance', 'expiry_month_card', 'expiry_year_card', 'cvc_card', )


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
