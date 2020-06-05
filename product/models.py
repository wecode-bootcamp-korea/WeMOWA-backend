from django.db import models

class Product(models.Model):
    name            = models.CharField(max_length = 50)
    price           = models.DecimalField(max_digits = 10, decimal_places = 2)
    collection      = models.ForeignKey('Collection',on_delete = models.SET_NULL, null=True)
    stock_status    = models.ForeignKey('StockStatus', on_delete = models.SET_NULL, null = True)
    category        = models.ForeignKey('Category', on_delete = models.SET_NULL, null = True)
    description	    = models.CharField(max_length = 1000)
    luggage_color   = models.CharField(max_length = 50, null=True)
    tag	            = models.ManyToManyField('Tag', through = 'ProductOption')
    handle          = models.ManyToManyField('Handle', through = 'ProductOption')
    wheel           = models.ManyToManyField('Wheel', through = 'ProductOption')
    detail          = models.TextField(null = True)
    product_number  = models.CharField(max_length = 50, null = True)
    texture         = models.ForeignKey('Texture', on_delete = models.SET_NULL, null = True)
    color_url       = models.URLField(max_length = 2000, null=True)

    class Meta:
        db_table = 'products'

class StockStatus(models.Model):
    name        = models.CharField(max_length = 50)

    class Meta:
        db_table = 'stock_status'

class Category(models.Model):
    name        = models.CharField(max_length = 50)

    class Meta:
        db_table = 'categories'

class Collection(models.Model):
    name        = models.CharField(max_length = 50)

    class Meta:
        db_table = 'collections'

class Image(models.Model):
    img_url 	= models.URLField(max_length = 2000)
    product 	= models.ForeignKey('Product', on_delete = models.SET_NULL, null = True, blank = True)

    class Meta:
        db_table = 'images'

class Texture(models.Model):
    name        = models.CharField(max_length = 50,null=True)

    class Meta:
        db_table = 'textures'

class ProductOption(models.Model):
    product     = models.ForeignKey('Product', on_delete = models.SET_NULL, null=True)
    tag         = models.ForeignKey('Tag', on_delete = models.SET_NULL, null = True)
    handle      = models.ForeignKey('Handle', on_delete = models.SET_NULL, null = True)
    wheel       = models.ForeignKey('Wheel', on_delete = models.SET_NULL, null = True)
    tag_text    = models.CharField(max_length  = 50, null=True)
    
    class Meta:
        db_table = 'products_options'

class Tag(models.Model):
    color       = models.CharField(max_length = 50)
    color_url   = models.URLField(max_length = 2000)

    class Meta:
        db_table = 'tags'

class Wheel(models.Model):
    color       = models.CharField(max_length = 50)

    class Meta:
        db_table = 'wheels'

class Handle(models.Model):
    color       = models.CharField(max_length = 50)

    class Meta:
        db_table = 'handles'

