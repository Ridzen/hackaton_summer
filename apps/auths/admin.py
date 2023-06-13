from django.contrib import admin
from .models import Users

# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    # Определите отображаемые поля
    list_display = ['name', 'email', 'surname', 'birth_date', 'username', 'password']
    # Определите поля для поиска
    search_fields = ['name', 'surname', 'email', 'username']
    # Определите фильтры
    list_filter = ['birth_date', 'name', 'surname', 'email', 'username']
