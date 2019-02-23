from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):
    name         = models.CharField(max_length=120)
    location     = models.CharField(max_length=120, null=True, blank=True)
    category	 = models.CharField(max_length=120,null=True, blank =True)
    timestamp	 = models.DateTimeField(auto_now = True)
    updated		 = models.DateTimeField(auto_now_add=True)
    my_date		 = models.DateField(auto_now=False,auto_now_add=False)

    def __str__(self):
    	return self.name
# class FoodAvail(models.Model):
# 	name     = models.CharField(max_length=120)
# 	food_type     = models.CharField(max_length=120, null=True, blank=True)      