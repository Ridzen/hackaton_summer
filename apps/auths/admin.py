from django.contrib import admin
from .models import Users, Profile


# Register your models here.


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):

    # Определите отображаемые поля
    list_display = ['email', 'password']
    # Определите поля для поиска
    search_fields = ['email']
    # Определите фильтры
    list_filter = ['email']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
