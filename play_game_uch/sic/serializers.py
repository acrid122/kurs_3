from rest_framework import serializers
from .models import *


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ['user', 'amount_true', 'amount_false', 'amount_all']