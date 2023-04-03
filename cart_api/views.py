from django.shortcuts import render
from . import models, serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.

class CartProductGetPost(generics.ListCreateAPIView):
    queryset = models.CartProduct.objects.all()
    serializer_class = serializers.CartProductSerializer

class CartPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

class CartGetPost(generics.ListCreateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

    
class CartProductPk(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CartProduct.objects.all()
    serializer_class = serializers.CartProductSerializer