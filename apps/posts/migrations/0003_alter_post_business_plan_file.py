# Generated by Django 4.2.2 on 2023-06-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='business_plan_file',
            field=models.CharField(max_length=500, verbose_name='Файл'),
        ),
    ]
