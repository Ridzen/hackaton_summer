from django.db import models

from apps.payment.choices import PAYMENT_CHOICES
from apps.posts.models import Post
from apps.wallet.models import Wallet


class Payment(models.Model):
    """Платеж"""
    status = models.CharField(
        max_length=25, choices=PAYMENT_CHOICES,
        verbose_name='Статус платежа'
    )
    sum_of_post = models.IntegerField(verbose_name="Вводимая сумма")
    is_transaction_finished = models.BooleanField(default=False, verbose_name="Транзакция закончена ли")
    wallet_id = models.ForeignKey(
        to=Wallet, on_delete=models.CASCADE,
        related_name="wallets", verbose_name="Кошелек"
    )
    post_id = models.ForeignKey(
        to=Post, on_delete=models.CASCADE,
        related_name="posts", verbose_name="Пост"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Создано"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Изменено"
    )

    def __str__(self):
        return f'Id: {self.id} and Status: {self.status}'

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
