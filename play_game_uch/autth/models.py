from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxLengthValidator, MinLengthValidator
from .manager import UserManager
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(
        validators = [
            MinLengthValidator(4)
        ]
    )
    email = models.EmailField(
        unique = True,
        validators = [
            MaxLengthValidator(254)
        ]
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_verified = models.BooleanField(default = False)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["login"]


    objects = UserManager()


    def __str__(self):
        return self.email
    
    
    @property
    def get_login(self):
        return f"{self.login}"

    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }


    class Meta:
        verbose_name_plural = 'Пользователи'


class OneTimePassword(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    code=models.CharField(max_length=6, unique=True)


    def __str__(self):
        return f"{self.user.login}-passcode"