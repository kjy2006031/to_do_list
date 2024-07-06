from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="list_index"),
    path('create', create_list, name="list_create"),
    path('delete/<int:list_id>/', delete_list, name="list_delete"),
    path('list/config/<int:list_id>/', list_config, name='list_config'),

]