from django.urls import path
from .views import RegistrationView, LoginView, LogoutView
from apps.auths.views import ProfileApiView
from rest_framework.routers import DefaultRouter as DR

router = DR()
router.register('profile', ProfileApiView, basename='profiles')


urlpatterns = [
    # Эндпоинт для регистрации пользователя
    path('register/', RegistrationView.as_view(), name='register'),
    # Эндпоинт для логин пользователя
    path('login/', LoginView.as_view(), name='login'),
    # Эндпоинт для логаут пользователя
    path('logout/', LogoutView.as_view(), name='logout'),
]

urlpatterns += router.urls

