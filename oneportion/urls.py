"""oneportion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import home.views
from django.conf import settings
from django.conf.urls.static import static
import search.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.main, name="main"),
    path('recipy/<int:dish_id>/', home.views.recipy, name="recommendrecipy"),
    path('accounts/', include('accounts.urls')),
    path('fridge/', include('fridge.urls')),
    path('expert/', include('expert.urls')),
    path('community/', include('community.urls')),
    path('bestrecipe/', include('bestrecipe.urls')),
    path('commentcrud/', include('commentcrud.urls')),
    path('result/', search.views.result, name='result'),
    path('search/', search.views.search, name='search'),
]
urlpatterns += [path('summernote/', include('django_summernote.urls'))]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

