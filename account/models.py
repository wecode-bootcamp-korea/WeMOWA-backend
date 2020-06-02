from django.db import models
from product.models import Product


class User(models.Model):
    first_name	= models.CharField(max_length = 100)
    last_name	= models.CharField(max_length = 100)
    email		= models.EmailField(max_length = 200, unique = True)
    password	= models.CharField(max_length = 200, unique = True)
    prefix		= models.ForeignKey('Prefix',on_delete = models.SET_NULL, null=True)
    created_at	= models.DateTimeField(auto_now_add = True)
    updated_at	= models.DateTimeField(auto_now = True)
    country		= models.CharField(max_length = 50)
    wishlist    = models.ManyToManyField(Product,through = 'UserWishlist')

    class Meta:
        db_table = 'users'

class Address(models.Model):
    name            = models.CharField(max_length = 50)
    st_address      = models.CharField(max_length = 300)
    op_address      = models.CharField(max_length = 500, null=True, blank = True)
    city            = models.CharField(max_length = 50)
    zip_code        = models.CharField(max_length = 50)
    phone_number    = models.CharField(max_length = 50)
    user            = models.ForeignKey('User',on_delete = models.SET_NULL,null=True)

    class Meta:
        db_table = 'addresses'

class Prefix(models.Model):
    name        = models.CharField(max_length = 50)
	
    class Meta:
        db_table = 'prefixes'

class RegisteredLuggage(models.Model):
    user			= models.ForeignKey('User', on_delete = models.SET_NULL, null = True)
    serial_number	= models.CharField(max_length = 100)
    purchase_date	= models.DateField()

    class Meta:
        db_table = 'registered_luggages'

class UserWishlist(models.Model):
    user            = models.ForeignKey('User', on_delete = models.SET_NULL, null = True)
    product	        = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'users_wishlists'

