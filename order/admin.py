from django.contrib import admin
from .models import PizzaOrder,Customer

# Register your models here.
admin.site.register(Customer)
admin.site.register(PizzaOrder)
