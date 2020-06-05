import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from .models import *
from account.utils import login_decorator

class ProductListView(View):
    def get(self,request,category_id):
        sort = request.GET.get('sort',None)
        if sort == 'PRICE LOW TO HIGH':
            product_list = Product.objects.select_related('collection').all().order_by('price')
        elif sort == 'PRICE HIGH TO LOW':
            product_list = Product.objects.select_related('collection').all().order_by('-price')
        elif sort == 'A-Z':
            product_list = Product.objects.select_related('collection').all().order_by('name')
        elif sort == 'Z-A':
            product_list = Product.objects.select_related('collection').all().order_by('-name')
        else:
            product_list = Product.objects.select_related('collection').all()

        color_filter = request.GET.getlist('color',[])
        price_filter = request.GET.get('price',None)
        collection_filter = request.GET.getlist('product_collection',[])
        filtered_obj = Product.objects.select_related('collection').all()
        if len(color_filter) > 0:
            obj = Product.objects.none()
            for color in color_filter:
                obj |= filtered_obj.filter(luggage_color__icontains = color.title())
            for product in obj:
            filtered_obj = obj
        if price_filter:
            price_filter = price_filter.split('-')
            min_price = int(price_filter[0].strip()[1:])
            max_price = int(price_filter[1].strip()[1:])
            filtered_obj = filtered_obj.filter(price__range = (min_price, max_price))
        if len(collection_filter) > 0:
            obj = Product.objects.none()
            for col in collection_filter:
                obj |= filtered_obj.filter(collection_id = Collection.objects.get(name = col))
            filtered_obj = obj
        product_list = filtered_obj
        search = request.GET.get('search', None)
        if search:
            product_list = Product.objects.select_related('collection').filter(Q(name__istartswith = search) | Q(collection__name__istartswith = search))
        result = []
        if int(category_id) == 1:
            product_list = product_list.exclude(category_id = 2)
        else:
            product_list = product_list.exclude(category_id = 1)
        for product in product_list:
            product_info = {}
            collection = product.collection.name
            name = product.name
            price = product.price
            color = product.luggage_color
            product_number = product.product_number
            product_id = product.id
            series_color = []

            for obj in Product.objects.filter(name = name, collection_id = product.collection.id):
                series_info = {}
                series_info['name'] = obj.luggage_color
                series_info['color_url'] = obj.color_url
                images = obj.image_set.all()
                series_info['product_img1'] = images[0].img_url
                series_info['product_img2'] = images[1].img_url
                series_color.append(series_info)
            product_info['collection'] = collection
            product_info['name'] = name
            product_info['product_id'] = product_id
            product_info['product_number'] = product_number
            product_info['price'] = price
            product_info['luggage_color'] = color
            product_info['series_color'] = series_color
            result.append(product_info)
        return JsonResponse({'data':result}, status = 200)


class ProductDetailView(View):
    @login_decorator
    def get(self,request):
        product_number = request.GET.get('product_number',None)
        product = Product.objects.select_related('collection','stock_status').get(product_number = product_number)
        if request.user != '':
            current_userid = request.user.id
        is_wished = False
        wished_by = product.userwishlist_set.all()
        if wished_by.exists():
            for wish in wished_by:
                if current_userid == wish.user_id:
                    is_wished = True
        series_color = []
        series = Product.objects.filter(name = product.name, collection_id = product.collection.id)
        result = {}
        result['collection'] = product.collection.name
        result['product_id'] = product.id
        result['name'] = product.name
        result['price'] = product.price
        result['stock_status'] = product.stock_status.name
        result['description'] = product.description
        result['color'] = product.luggage_color
        result['images'] = list(product.image_set.values())
        result['color_urls'] = [item.color_url for item in series]
        result['color_product_numbers'] = [item.product_number for item in series]
        result['innerHTML'] = product.detail
        result['wishlist'] = is_wished
        return JsonResponse({'data':result}, status = 200)
