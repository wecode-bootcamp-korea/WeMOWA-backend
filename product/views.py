mport json
from django.shortcuts import render
from django.view import View
from .models import *
from django.http import HttpResponse, JsonResponse


class ProductListView(View):
    def get(self,request):
        sort = request.GET('sort',None)
        if sort == 'PRICE LOW TO HIGH':
            product_list = list(Product.objects.values().order_by('price'))
        elif sort == 'PRICE HIGH TO LOW':
            product_list = list(Product.objects.values().order_by('-price'))
        elif sort == 'A-Z':
            product_list = list(Product.objects.values().order_by('name'))
        elif sort == 'Z-A':
            product_list = list(Product.objects.values().order_by('-name'))
        else:
            product_list = list(Produc.objects.values())
#        filter_options = request.GET('filter',None)

        product = {}
        series_color = {}
        for product in product_lst:
            collection = Collection.objects.get(id=collection_id).name
            name = product['name']
            price = product['price']
            color = product['luggage_color']
            for obj in Product.objects.filter(name = name and collection_id = collection_id):
                series_color[obj.luggage_color] = [obj.color_url]
                images = Image.objects.filter(product_id = obj.id)
                for i in range(2):
                    series_color[obj.luggage_color].append(images[i].img_url)
           product['collection'] = collection
           product['name'] = name
           product['price'] = price
           product['luggage_color'] = color
           product['series_color'] = series_color
        return JsonResponse({'data':product}, status = 200)




