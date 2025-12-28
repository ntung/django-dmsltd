from django.contrib import admin
from .models import Drink, DrinkCategory

# Register your models here.
admin.site.register(Drink)
admin.site.register(DrinkCategory)