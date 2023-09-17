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
    business_plan_file = models.CharField(
        max_length=500, verbose_name='Файл'
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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    """Post Comments"""
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Пользователь'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Пост'
    )
    parent_comment = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE,
        related_name='replies', verbose_name='Родительский комментарий'
    )
    content = models.TextField(
        verbose_name='Содержание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )

    def __str__(self):
        return f'{self.user.username} - {self.post.title} - {self.content}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Like(models.Model):
    user = models.ForeignKey(
        Profile, on_delete=models.CASCADE,
        related_name='likes', verbose_name='Пользователь'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Публикация',
        related_name='likes'
    )

    def __str__(self):
        return f'{self.post.title} - {self.user.username}'

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        unique_together = ('user', 'post')
