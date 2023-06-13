from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.exceptions import ValidationError
# Create your models here.


""" 
Создание автоматической двух функций основанных на генерации моделек 
"""


class BaseUserAccountManager(BaseUserManager):

    def create_user(self, email, name=None, surname=None, birthday=None, password=None, **extra_fields):
        if not email:
            raise ValidationError('Пользователь должен иметь email')  # Проверка двух видов валидации на ошибку
        if not name:
            raise ValidationError('Пользователь должен иметь name ')  # Это первый тип
        if not surname:
            raise ValueError('Пользователь должен иметь surname')  # Это второй тип

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            birthday=birthday,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):

        if not email:
            raise ValidationError('Суперпользователь должен иметь email')
        if not password:
            raise ValidationError('Суперпользователь должен иметь password')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Users(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email', max_length=60, unique=True, blank=True, null=True, default=None,
        help_text='Элетронная почта'
    )
    name = models.CharField(
        max_length=30, blank=True, null=True, verbose_name='Имя', help_text='Имя пользователя'
    )
    surname = models.CharField(
        max_length=30, blank=True, null=True, verbose_name='Фамилия', help_text='Фамилия пользователя'
    )
    username = models.CharField(
        max_length=60, blank=True, null=True, unique=True, verbose_name='Никнэйм', help_text='Никнейм пользователя'
    )
    birth_date = models.CharField(
        max_length=30, blank=True, null=True, default=None, verbose_name='Дата рождения'
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
