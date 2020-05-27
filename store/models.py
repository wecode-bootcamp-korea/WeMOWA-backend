from django.db import models

class Store(models.Model):
	lat 		= models.FloatField()
	lng 		= models.FloatField()
	name 		= models.CharField(max_length = 200)
	address 	= models.CharField(max_length = 200)
	city 		= models.CharField(max_length = 50)
	postal_code 	= models.CharField(max_length = 50)
	store_type 	= models.ManyToManyField('StoreType', through = 'StoreStoreType')
	img_url 	= models.CharField(max_length = 2000)

	class Meta:
		db_table = 'stores'
	

class StoreType(models.Model):
	name 		= models.CharField(max_length = 50)

	class Meta:
		db_table = 'store_types'

class StoreStoreType(models.Model):
	store 		= models.ForeignKey('Store', on_delete = models.SET_NULL, null = True)
	store_type 	= models.ForeignKey('StoreType', on_delete = models.SET_NULL, null = True)

	class Meta:
		db_table = 'store_store_types'

