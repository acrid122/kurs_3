from django.contrib import admin
from .models import *


class StatAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount_all', 'amount_true', 'amount_false')
    #list_display = (stat)
    search_fields = ('user', 'amount_all')
admin.site.register(Stat, StatAdmin)
