from django.contrib import admin
from .models import User,MenuCategory,MenuItem,Order,Waiter,Reception,Bill

# Register your models here.

admin.site.register(User)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(Waiter)
admin.site.register(Reception)
admin.site.register(Bill)



