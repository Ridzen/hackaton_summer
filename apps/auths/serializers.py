from rest_framework import serializers

from apps.auths.models import Users, Profile


class RegistrationSerializer(serializers.ModelSerializer):
    """Сериалайзер для регистрации"""
    class Meta:
        model = Users
        fields = (
            "email",
            "password"
        )
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Users.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    """Сериалайзер для пользователя"""
    class Meta:
        model = Users
        fields = (
            "id",
            "email",
            "password",
        )


class ProfileSerializer(serializers.ModelSerializer):
    """Профиль пользователя"""
    class Meta:
        model = Profile
        fields = (
            "id",
            "user_profile",
            "username",
            "user_image",
            "bio",
            "instagram_link",
            "birth_date"
        )

