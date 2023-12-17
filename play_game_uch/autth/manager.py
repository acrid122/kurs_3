from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import logging


class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            RegexValidator(
                regex = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$',
            )
        except ValidationError:
            raise ValueError(_("Пожалуйста, введите валидный email!"))
        
        

    def create(self, login, email, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("Пожалуйста, введите email!")
        if not login:
            raise ValueError("Пожалуйста, введите логин!")
        user = self.model(login = login, email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    

    def create_superuser(self, login, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Вы не администратор")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Вы не администратор")
        
        user=self.create(
            login, email, password, **extra_fields
        )
        user.save(using=self.db)
        return user
