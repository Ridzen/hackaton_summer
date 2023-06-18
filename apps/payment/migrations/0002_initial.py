# Generated by Django 4.2.2 on 2023-06-18 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.post', verbose_name='Пост'),
        ),
    ]
