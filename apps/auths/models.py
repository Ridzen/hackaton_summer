from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import gettext_lazy as _

""" 
Создание автоматической двух функций основанных на генерации моделек 
"""


class BaseUserAccountManager(BaseUserManager):
    """Менеждер"""

    def create_user(self, email: str, password: str, **extra_fields):
        """Создание пользователя"""
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        """Создание суперпользователя"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class Users(AbstractBaseUser):
    """Пользователь"""
    email = models.EmailField(
        verbose_name='email', max_length=60, unique=True,
        blank=True, null=True, default=None,
        help_text='Элетронная почта'
    )

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_simple_user = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = BaseUserAccountManager()

    class Meta:
        db_table = "tbl_users"
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser


class Profile(models.Model):
    """Профиль пользователя"""
    user_profile = models.OneToOneField(
        Users, on_delete=models.CASCADE, blank=False,
        null=False, unique=True, verbose_name='Чей профиль', help_text='Профиль', related_name='profile'
    )
    username = models.CharField(
        max_length=60, blank=True, null=True, unique=True, verbose_name='ФИО', help_text='ФИО'
    )
    user_image = models.ImageField(
        blank=True, null=True, verbose_name='Аватарка на профиль', help_text='Аватар'
    )
    bio = models.TextField(
        blank=True, null=True, verbose_name='Биография владельца'
    )
    instagram_link = models.TextField(
        blank=True, null=True, verbose_name='Ссылка на профиль в инстграмме'
    )
    birth_date = models.CharField(
        max_length=30, blank=True, null=True, default=None, verbose_name='Дата рождения'
    )

    def __str__(self):
        return f'User:{self.user_profile} and username: {self.username}'

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
