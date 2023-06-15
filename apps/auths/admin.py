from django.contrib import admin
from .models import Users

# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    # Определите отображаемые поля

    list_display = ['email', 'birth_date', 'password']
    # Определите поля для поиска
    search_fields = ['email']
    # Определите фильтры
    list_filter = ['email']
