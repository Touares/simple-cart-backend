from django.db import models

# Create your models here.


class Cart(models.Model):
    totalQuantity = models.IntegerField()

    def __str__(self) -> str:
        return str(self.id)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,related_name='cartProduct', on_delete=models.CASCADE)
    name =models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_id =  models.IntegerField()
    quantity = models.IntegerField()
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.name
    

# id: newItem.id,
#                     price:newItem.price,
#                     quantity: 1,
#                     totalPrice:newItem.price,
#                     name: newItem.name
    
