from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import ConfirmationCode

class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data['username']
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Пользователь с таким именем уже существует.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = False  # Пользователь не активен до подтверждения
        user.save()
        
        code = ConfirmationCode.objects.create(user=user, code=ConfirmationCode.generate_code())
        # Здесь отправить email с кодом подтверждения (не забыть конфигурацию для send_mail)
        
        return user

import logging

logger = logging.getLogger(__name__)

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Проверяем, существует ли пользователь с таким именем
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            logger.error(f"Пользователь с именем {data['username']} не найден.")
            raise serializers.ValidationError("Пользователь не найден.")

        # Если пользователь найден, пытаемся аутентифицировать
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            logger.error(f"Не удалось аутентифицировать пользователя {data['username']} с паролем {data['password']}.")
            raise serializers.ValidationError("Неверные учетные данные.")
        
        return {'user': user}


class ConfirmUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    confirmation_code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
            code_record = ConfirmationCode.objects.get(user=user)
        except (User.DoesNotExist, ConfirmationCode.DoesNotExist):
            raise serializers.ValidationError("Неверный код или пользователь не найден.")
        if code_record.code != data['confirmation_code']:
            raise serializers.ValidationError("Неверный код подтверждения.")
        return data
