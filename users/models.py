from django.contrib.auth.models import User
from django.db import models
import random
from django.core.exceptions import ValidationError

def validate_code(value):
    """Проверяет, что код состоит из 6 цифр"""
    if not value.isdigit() or len(value) != 6:
        raise ValidationError("Код подтверждения должен состоять из 6 цифр.")

class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, validators=[validate_code])

    @staticmethod
    def generate_code():
        return str(random.randint(100000, 999999))
