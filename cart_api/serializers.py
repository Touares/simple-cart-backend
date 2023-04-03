from rest_framework import serializers
from .models import CartProduct, Cart
from drf_writable_nested.serializers import WritableNestedModelSerializer


class CartProductSerializer(serializers.ModelSerializer):
    # cart = serializers.SlugRelatedField(
        # queryset=Cart.objects.all(), slug_field='id')
    class Meta:
        model = CartProduct
        fields = ['id', 'name', 'price', 'item_id', 
                  'quantity', 'totalPrice']
        depth = 1


class CartSerializer(WritableNestedModelSerializer):
    cartProduct = CartProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['id', 'totalQuantity', 'cartProduct']
        depth = 1

        