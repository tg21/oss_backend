from django.contrib import admin

from .models import user,item,category,cart,order,inventory
# Register your models here.

admin.site.register(user)
admin.site.register(item)
admin.site.register(category)
admin.site.register(cart)
admin.site.register(order)
admin.site.register(inventory)