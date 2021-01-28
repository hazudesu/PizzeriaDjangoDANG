from pizzastore.models import Order, Pizza, Topping
from django.contrib import admin

# Register your models here.
'''Registro de modelos para acceso facil desde el admin de Django
'''
admin.site.register(Order)
admin.site.register(Topping)
admin.site.register(Pizza)
