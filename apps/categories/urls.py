from django.urls import path
from apps.categories.views import CategoryView

urlpatterns = [
    path('add-category/', CategoryView.as_view(), name='category-view')
]
