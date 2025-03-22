from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/register/', views.register_user_view),  # Путь для регистрации
    path('api/v1/login/', views.login_user_view),        # Путь для логина
    path('api/v1/confirm/', views.confirm_user_view),    # Путь для подтверждения
]
