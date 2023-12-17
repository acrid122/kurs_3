import random
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.conf import settings


def generate_pass():
    code = ""
    for _ in range(6):
        code += str(random.randint(1,9))
    return code


def send_code_user(email):
    subject = "Код для верификации email!"
    code = generate_pass()
    user = User.objects.get(email=email)
    email_body = f"Привет! Спасибо за регистрацию на нашей платформе! Твой код для подтверждения email: {code}"
    from_email = settings.DEFAULT_FROM_EMAIL
    OneTimePassword.objects.create(user=user, code=code)
    send_email = EmailMessage(subject=subject, body=email_body,from_email=from_email,to=[email])
    send_email.send(fail_silently=True)


def send_normal_email(data):
    email=EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email=settings.EMAIL_HOST_USER,
        to=[data['to_email']]
    )
    email.send()