from django.db import models


class Category(models.Model):
    """Категория"""
    title = models.CharField(max_length=155, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
