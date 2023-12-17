from django.urls import path
from .views import *

urlpatterns = [
    path('stat/', StatView.as_view(), name = "Полная статистика"),
    path('stat/<int:user_id>/', UserStatView.as_view(), name='user-stat')
]