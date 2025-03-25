from django.urls import path
from .views import RegisterUserView, LoginUserView, ConfirmUserView

urlpatterns = [
    path('api/v1/register/', RegisterUserView.as_view()),
    path('api/v1/login/', LoginUserView.as_view()),
    path('api/v1/confirm/', ConfirmUserView.as_view()),
]
