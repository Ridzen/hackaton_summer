# Generated by Django 4.2.2 on 2023-06-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_owner',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]
