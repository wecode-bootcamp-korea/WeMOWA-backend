import json
from django.shortcuts import render
from django.view import View
from .models import *
from django.http import HttpResponse, JsonResponse


class ProductListView(View):
    def get(self,request):
        series_color = {}
        product_list = list(Product.objects.values())
        for product in product_lst:
            collection_id = product['collection_id']
            collection = Collection.objects.get(id=collection_id).name
            name = product['name']
            price = product['price']
            color = product['luggage_color']
            for obj in Product.objects.filter(name = name and collection_id = collection_id):
                series_color[obj.luggage_color] = [obj.color_url]
            images = Image.objects.filter(product_id = product['id'])
            series_color[color].append(images[0].img_url)
            series_color[color].append(images[1].img_url)
            series_color['colleciton'] = collection

