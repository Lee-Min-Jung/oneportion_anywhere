from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404
from fridge.models import Dish
from community.models import Post
from expert.models import Expert
from django.db.models import Max
import random

def get_random_dish():
    #max_id = Dish.objects.all().exclude(image='ttgaogawdwdfmexebiwz.jpg').aggregate(max_id=Max("id"))['max_id']
    #max_id = Dish.objects.all().aggregate(max_id=Max("id"))['max_id']
    max_id = 26
    while True:
        pk = random.randint(1, max_id) #
        dish = Dish.objects.filter(pk=pk).first()
        if dish:
            return dish

def main(request):
    todaydish = get_random_dish() #
    return render(request, 'main.html', {'todaydish': todaydish})


def recipy(request, dish_id):
    dish_recipy = get_object_or_404(Dish, pk = dish_id)
    post_object = Post.objects.all()
    expert_object = Expert.objects.all()

    if dish_recipy:
        result = post_object.filter (title__contains=dish_recipy) | post_object.filter(content__contains = dish_recipy)
        result2 = expert_object.filter (title__contains = dish_recipy) | expert_object.filter(body__contains = dish_recipy)
    return render(request, 'recipy.html', {'dish' : dish_recipy, 'result': result, 'result2':result2})