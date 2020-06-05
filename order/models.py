from django.db import models
from account.models import User
from product.models import  Product, Tag, Handle, Wheel

class Order(models.Model):
    user         = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    order_status = models.ForeignKey('OrderStatus', on_delete = models.SET_NULL, null = True)
    created_at   = models.DateTimeField(auto_now_add = True)
    product      = models.ManyToManyField(Product, through = 'Cart')

    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'orders_status'

class Cart(models.Model):
    order   = models.ForeignKey('Order', on_delete = models.SET_NULL, null= True)
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
    amount  = models.IntegerField()
    tag     = models.ForeignKey(Tag, on_delete = models.SET_NULL, null = True, blank = True)
    handle  = models.ForeignKey(Handle, on_delete = models.SET_NULL, null = True, blank = True)
    wheel   = models.ForeignKey(Wheel, on_delete = models.SET_NULL, null = True, blank = True)

    class Meta:
        db_table	= 'carts'

