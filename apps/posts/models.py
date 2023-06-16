from django.db import models

from apps.auths.models import Profile
from apps.categories.models import Category


class Post(models.Model):
    """Post Model"""
    title = models.CharField(
        max_length=155, verbose_name="Название"
    )
    category_id = models.ForeignKey(
        to=Category, on_delete=models.CASCADE,
        related_name="categories", verbose_name="Категория"
    )
    short_info = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Краткая информация'
    )
    status = models.BooleanField(
        default=False, verbose_name='Статус'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Создано"
    )
    user_profile_id = models.ForeignKey(
        to=Profile, on_delete=models.CASCADE,
        related_name="profiles", verbose_name="Пользователь"
    )
    full_info = models.CharField(
        max_length=500, verbose_name='Полная информация'
    )
    business_plan_file = models.FileField(
         upload_to='media/business_documents', verbose_name="Файлы"
    )
    amount = models.IntegerField(
        verbose_name="Общая запрашиваемая сумма"
    )
    amount_rest = models.IntegerField(
        verbose_name="Сколько осталось"
    )
    amount_per_season = models.IntegerField(
        verbose_name="Сколько с человека"
    )
    amount_of_person = models.IntegerField(
        verbose_name="Сколько людей уже согласилось"
    )
