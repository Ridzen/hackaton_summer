# Generated by Django 4.2.2 on 2023-06-18 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wallet', '0001_initial'),
        ('payment', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='wallet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallets', to='wallet.wallet', verbose_name='Кошелек'),
        ),
    ]