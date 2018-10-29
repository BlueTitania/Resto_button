from django.shortcuts import render
from restaurant.models import Restaurant

def restaurant(request, name, res_id) :
    restaurant = Restaurant.objects.get(name=name, id=res_id)

    return render(request, 'datail.html')

def main_page(request) :

    return render(request, 'index.html')
