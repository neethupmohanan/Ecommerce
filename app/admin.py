from django.contrib import admin

from .models import Cart, product, address, order

# Register your models here.
admin.site.register(product)
admin.site.register(Cart)
admin.site.register(address)
admin.site.register(order)

