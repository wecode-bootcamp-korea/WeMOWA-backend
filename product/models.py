from django.db import models


class Product(models.Model):
	name 		= models.CharField(max_length = 50)
	price		= models.DecimalField(max_digits = 10, decimal_places = 2)
	collection	= models.CharField(max_length = 50)
	stock_status	= models.ForeignKey('StockStatus', on_delete = models.SET_NULL, null = True, blank = True)
	category	= models.ForeignKey('Category', on_delete = models.SET_NULL, null = True, blank = True)
	sub_category	= models.ForeignKey('SubCategory', on_delete = models.SET_NULL, null = True, blank = True)
	product_number	= models.CharField(max_length = 50)
	description	= models.CharField(max_length = 1000)
	material	= models.ForeignKey('Material', on_delete = models.SET_NULL, null = True, blank = True)
	luggage_color	= models.ManyToManyField('LuggageColor', through = 'ProductLuggageColor', null = True, blank = True)
	tag		= models.ManyToManyField('Tag', through = 'ProductOption', null = True, blank = True)
	handle		= models.ManyToManyField('Handle', through = 'ProductOption', null = True, blank = True)
	wheel		= models.ManyToManyField('Wheel', through = 'ProductOption', null = True, blank = True)

	class Meta:
		db_table = 'products'

class StockStatus(models.Model):
	name 		= models.CharField(max_length = 50)

	class Meta:
		db_table = 'stock_status'

class Category(models.Model):
	name 		= models.CharField(max_length = 50)

	class Meta:
		db_table = 'categories'

class SubCategory(models.Model):
	name 		= models.CharField(max_length = 50)

	class Meta:
		db_table = 'sub_categories'

class Image(models.Model):
	img_url 	= model.CharField(max_length = 2000)
	product 	= model.ForeignKey('Product', on_delete = models.SET_NULL, null = True, blank = True)
	
	class Meta:
		db_table = 'images'

class Material(models.Model):
	name 		= model.CharField(max_length = 50)

	class Meta:
		db_table = 'materials'

class LuggageColor(models.Model):
	color 		= models.CharField(max_length = 50)
	color_url 	= models.CharField(max_length = 1000)
	texture 	= models.ForeignKey('Texture', on_delete = models.SET_NULL, null = True)

	class Meta:
		db_table = 'luggage_colors'

class Texture(models.Model):
	name 		= models.CharField(max_length = 50)

	class Meta:
		db_table = 'textures'

class ProductLuggageColor(models.Model):
	luggage_color 	= models.ForeignKey('LuggageColor', on_delete = models.SET_NULL, null = True)
	product 	= models.ForeignKey('Product', on_delete = models.SET_NULL, null = True)

	class Meta:
		db_table = 'products_luggage_colors'

class ProductOption(models.Model):
	product 	= models.ForeignKey('Product', on_delete = models.SET_NULL, null = True, blank = True)
	tag 		= models.ForeignKey('Tag', on_delete = models.SET_NULL, null = True, blank = True)
	handle 		= models.ForeignKey('Handle', on_delete = models.SET_NULL, null = True, blank = True)
	wheel 		= models.ForeignKey('Wheel', on_delete = models.SET_NULL, null = True, blank = True)

	class Meta:
		db_table = 'products_options'

class Tag(models.Model):
	color 		= models.CharField(max_length = 50)
	color_url 	= models.CharField(max_length = 2000)
	text 		= models.CharField(max_length = 50, null = True)

	class Meta:
		db_table = 'tags'

class Wheel(models.Model):
	color 		= models.CharField(max_length = 50)
        color_url 	= models.CharField(max_length = 2000)

	class Meta:
		db_table = 'wheels'

class Handle(models.Model):
	color 		= models.CharField(max_length = 50)
        color_url 	= models.CharField(max_length = 2000) 
	
	class Meta:
		db_table = 'handles'
	

	

