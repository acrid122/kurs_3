# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Stat

User = get_user_model()

@receiver(post_save, sender=User)
def create_stat(sender, instance, created, **kwargs):
    if created:
        Stat.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_stat(sender, instance, **kwargs):
    instance.statistics.save()
