from django.db import models

from apps.auths.models import Profile


class Wallet(models.Model):
    """Кошелек"""
    owner = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="wallet", verbose_name='Владелец'
    )
    rs_number = models.CharField(max_length=150, verbose_name="Расчетный счет нашей системы")
    balance = models.IntegerField(default=0, verbose_name="Баланс кошелька")
    expiry_month = models.CharField(max_length=150, verbose_name="Месяц истечения")
    expiry_year = models.CharField(max_length=150, verbose_name="Год истечения")
    cvc = models.CharField(max_length=150, verbose_name="CVC")

    def __str__(self):
        return f"Wallet of {self.owner} with {self.balance}"

    class Meta:
        verbose_name = "Кошелек"
        verbose_name_plural = "Кошельки"
