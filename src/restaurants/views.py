import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
#Create your views here.

from .models import RestaurantLocation

class RandomView(TemplateView):
    template_name = 'random_number.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RandomView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [
            random.randint(0, 100), 
            random.randint(0, 100), 
            random.randint(0, 100)
        ]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 100)
        context = {
            "num": num, 
            "some_list": some_list
        }
        return context


def restaurant_listview(request):
    template_name= 'restaurants/restaurants_list.html'
    queryset     =  RestaurantLocation.objects.all()
    context = {
    "object_list": queryset
    }
    return render(request, template_name, context)


















