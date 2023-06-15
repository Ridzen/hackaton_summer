from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

""" 
Создание автоматической двух функций основанных на генерации моделек 
"""


class BaseUserAccountManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class Users(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email', max_length=60, unique=True,
        blank=True, null=True, default=None,
        help_text='Элетронная почта'
    )
    name = models.CharField(
        max_length=30, blank=True, null=True,
        verbose_name='Имя', help_text='Имя пользователя'
    )
    surname = models.CharField(
        max_length=30, blank=True, null=True,
        verbose_name='Фамилия', help_text='Фамилия пользователя'
    )
    username = models.CharField(
        max_length=60, blank=True, null=True, unique=True,
        verbose_name='Никнэйм', help_text='Никнейм пользователя'
    )
    birth_date = models.CharField(
        max_length=30, blank=True, null=True,
        default=None, verbose_name='Дата рождения'
    )

    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_simple_user = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_owner = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = BaseUserAccountManager()

    class Meta:
        db_table = "tbl_users"

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser
