# Generated by Django 4.2.2 on 2023-06-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, default=None, help_text='Элетронная почта', max_length=60, null=True, unique=True, verbose_name='email')),
                ('name', models.CharField(blank=True, help_text='Имя пользователя', max_length=30, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, help_text='Фамилия пользователя', max_length=30, null=True, verbose_name='Фамилия')),
                ('username', models.CharField(blank=True, help_text='Никнейм пользователя', max_length=60, null=True, unique=True, verbose_name='Никнэйм')),
                ('birth_date', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Дата рождения')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_simple_user', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_owner', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'tbl_users',
            },
        ),
    ]
