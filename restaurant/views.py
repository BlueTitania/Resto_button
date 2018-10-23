from django.shortcuts import render
from restaurant.models import Restaurant

def restaurant(request, name, res_id) :
    restaurant = Restaurant.objects.get(name=name, id=res_id)

    return render(request, 'test.html')

def main_page(request) :
    #restaurant = Restaurant.objects.get(name=name, id=res_id)

    return render(request, 'main_page.html')
