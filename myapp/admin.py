from django.contrib import admin
from .models import Drink, DrinkCategory, Booking

# Register your models here.
admin.site.register(Drink)
admin.site.register(DrinkCategory)
admin.site.register(Booking)
admin.site.site_header = "Thanh Binh Restaurant Admin"
admin.site.site_title = "Thanh Binh Restaurant Admin Portal"
admin.site.index_title = "Welcome to Thanh Binh Restaurant Admin Portal"