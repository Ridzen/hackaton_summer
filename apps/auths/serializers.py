from rest_framework import serializers

from apps.auths.models import Users


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Users.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = Users
        fields = [
            "email",
            "username",
            "name",
            'surname',
            "birth_date",
            "password",
        ]
