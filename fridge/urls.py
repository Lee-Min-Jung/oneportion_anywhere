from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.myfridge, name='myfridge'),
    path('showdish/', views.showdish, name='showdish'),
    path('showdish/recipy/<int:dish_id>', views.recipy, name="recipy")
]