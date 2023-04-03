from os import name
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
path('cart_get_post', views.CartGetPost.as_view(), name='cart_get_post'),
path('cp_get_post', views.CartProductGetPost.as_view(), name='cp_get_post'),
path('cart_pk/<int:pk>', views.CartPk.as_view(), name='cart_pk'),
path('cp_pk/<int:pk>', views.CartProductPk.as_view(), name='cp_pk'),

]