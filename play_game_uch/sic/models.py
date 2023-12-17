from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


class Stat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="statistics", primary_key = True)
    amount_true = models.CharField(default = 0)
    amount_false=models.CharField(default=0)
    amount_all = models.CharField(default = 0)


    def __str__(self):
        return f'Статистика по пользовател. {self.user.email}'


    class Meta:
        verbose_name_plural = 'Статистика по пользователям'
