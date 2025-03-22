from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from .serializers import RegisterUserSerializer, LoginUserSerializer, ConfirmUserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user_view(request):
    data = request.data
    try:
        serializer = RegisterUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Пользователь успешно зарегистрирован."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user_view(request):
    data = request.data
    try:
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid():  # Проверяем, что данные валидны
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)  # Создаем токен
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([AllowAny])
def confirm_user_view(request):
    data = request.data
    try:
        serializer = ConfirmUserSerializer(data=data)
        if serializer.is_valid():
            return Response({"message": "Аккаунт подтвержден."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
