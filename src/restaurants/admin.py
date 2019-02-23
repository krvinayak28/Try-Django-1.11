from django.contrib import admin

# Register your models here.
from .models import RestaurantLocation   #,FoodAvail

admin.site.register(RestaurantLocation) 
#admin.site.register(FoodAvail)