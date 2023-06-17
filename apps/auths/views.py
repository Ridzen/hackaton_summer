from rest_framework import (
    status, generics
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)
from rest_framework.authtoken.models import Token

from django.contrib.auth import (
    authenticate, login, logout
)
from django.contrib.auth.models import update_last_login
from rest_framework.viewsets import ModelViewSet


from apps.auths.serializers import (
    RegistrationSerializer, LoginSerializer, ProfileSerializer
)
from apps.auths.models import Profile


class RegistrationView(generics.CreateAPIView):
    """View для регистрации"""
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class LoginView(generics.CreateAPIView):
    """View для логина"""
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            update_last_login(None, user)
            return Response(
                {'token': token.key, 'message': 'Login successful.'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'message': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )


class LogoutView(APIView):
    """View для пользователя"""
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out successfully.'}, status=status.HTTP_200_OK)


class ProfileApiView(ModelViewSet):
    """Профиль для позователя CRUD"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
