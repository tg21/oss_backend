from django.contrib import admin

from .models import user,item
# Register your models here.

admin.site.register(user)
admin.site.register(item)