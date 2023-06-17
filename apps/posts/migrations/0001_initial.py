# Generated by Django 4.2.2 on 2023-06-16 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auths', '0006_remove_users_birth_date_remove_users_name_and_more'),
        ('categories', '0002_alter_category_options_alter_category_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Название')),
                ('short_info', models.CharField(blank=True, max_length=255, null=True, verbose_name='Краткая информация')),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('full_info', models.CharField(max_length=500, verbose_name='Полная информация')),
                ('business_plan_file', models.FileField(upload_to='media/business_documents', verbose_name='Файлы')),
                ('amount', models.IntegerField(verbose_name='Общая запрашиваемая сумма')),
                ('amount_rest', models.IntegerField(verbose_name='Сколько осталось')),
                ('amount_per_season', models.IntegerField(verbose_name='Сколько с человека')),
                ('amount_of_person', models.IntegerField(verbose_name='Сколько людей уже согласилось')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='categories.category', verbose_name='Категория')),
                ('user_profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='auths.profile', verbose_name='Пользователь')),
            ],
        ),
    ]