from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('login', 'email')
    #list_display = (stat)
    search_fields = ('login', 'email')
admin.site.register(User, UserAdmin)
admin.site.register(OneTimePassword)