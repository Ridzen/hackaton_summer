from datetime import datetime, timezone

from django.db import transaction
from rest_framework import serializers, exceptions

from apps.payment.choices import PAYMENT_CHOICES
from apps.payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Сериалайзер для платежа"""
    class Meta:
        model = Payment
        fields = (
            'id', 'sum_of_post',
            'wallet_id', 'post_id',
            'created_at', 'updated_at'
        )
        read_only_fields = ('created_at', 'updated_at')

    @transaction.atomic
    def create(self, validated_data):
        sum_of_post = validated_data.get("sum_of_post")
        wallet_id = validated_data.get("wallet_id")
        post_id = validated_data.get("post_id")

        if sum_of_post != post_id.amount_per_season or sum_of_post > wallet_id.balance \
                or post_id.amount_per_season * post_id.amount_of_person > post_id.amount:
            raise exceptions.ValidationError(
                {"Value error": "There are not enough funds on your balance "
                                "or is not similar with post amount pre season"}
            )

        wallet_id.balance -= sum_of_post
        wallet_id.save()

        post_id.amount_of_person += 1
        post_id.save()

        post_id.amount_rest = post_id.amount - sum_of_post
        post_id.save()

        payment = Payment.objects.create(**validated_data, status=PAYMENT_CHOICES[0][0])
        return payment


class PaymentFinishSerializer(serializers.ModelSerializer):
    """Finish Payment Serializer"""

    class Meta:
        model = Payment
        fields = (
            'id',
        )

    @transaction.atomic
    def update(self, instance, validated_data):
        if instance.status == PAYMENT_CHOICES[0][0]:
            instance.is_transaction_finished = True
            instance.save()

        if instance.is_transaction_finished:
            instance.status = PAYMENT_CHOICES[2]
            instance.save()
        else:
            raise exceptions.ValidationError({"Value error": "Sorry, but we don't create payment"})

        return instance


class PaymentRollbackSerializer(serializers.ModelSerializer):
    """Rollback Payment"""
    class Meta:
        model = Payment
        fields = (
            'id',
        )

    @transaction.atomic
    def update(self, instance, validated_data):
        if instance.status == PAYMENT_CHOICES[0]:
            instance.status = PAYMENT_CHOICES[3]
            instance.save()

        milli = abs(instance.updated_at - datetime.now(timezone.utc))
        type(milli)

        if milli.total_seconds() > 3600000 and instance.status == PAYMENT_CHOICES[2]:
            instance.status = PAYMENT_CHOICES[3]
            instance.save()
        else:
            raise exceptions.ValidationError({"Value error": "Sorry, but we don't rollback payment"})

        return instance
