from django.db.models.query_utils import Q
from django.shortcuts import render
from fridge.models import Dish
from django.db.models import Max
import random

def get_random_dish():
    max_id = Dish.objects.all().exclude(image='loaddish.jpg').aggregate(max_id=Max("id"))['max_id']
    while True:
        pk = random.randint(1, max_id)
        dish = Dish.objects.filter(pk=pk).exclude(Q(image='loaddish.jpg')|Q(image='')).first()
        if dish:
            return dish

def main(request):
    todaydish = get_random_dish()
    return render(request, 'main.html', {'todaydish': todaydish})