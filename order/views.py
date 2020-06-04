import json
from django.shortcuts import render
from django.views import  View
from django.http import HttpResponse, JsonResponse
from .models import Cart, Order, OrderStatus
from product.models import Product, ProductOption, Tag
from account.utils import login_decorator
    

class CartView(View):
    @login_decorator
    def post(self,request):
        data = json.loads(request.body)
        try:
            cart_item =  Product.objects.select_related('category','collection','texture','stock_status').prefetch_related('tag','cart_set','cart_set__order').get(product_number = data['product_number'])
            if "tag" in data:
                ProductOption.objects.create(
                    product_id  = cart_item.id,
                    tag_id      = Tag.objects.get(color = data['tag']).id,
                    tag_text    = data['tag_text']
                )
            if Cart.objects.filter( product_id = data['product_id']).exists():
                item = Cart.objects.get(product_id = data['product_id'])
                item.amount += 1
                item.save()
                return HttpResponse(status = 200)
            else:
                order_item = Order.objects.create(
                    user_id = request.user.id,
                    order_status_id = 1
                )
                Cart.objects.create(
                product_id      = cart_item.id,
                amount          = data['amount'],
                tag_id          = Tag.objects.get(color = data['tag']).id,
                order_id     = order_item.id
                )
                return HttpResponse( status = 200 )

        except KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' }, status = 400)

    @login_decorator
    def get(self,request):
        try:
            cart_list = [{
                'id'                : item.id,
                'collection_id'     : item.product.collection_id,
                'name'              : item.product.name,
                'price'             : item.product.price,
                'luggage_color'     : item.product.luggage_color,
                'stock_status_id'   : item.product.stock_status_id,
                'amount'            : item.amount,
                'image'             : item.product.image_set.all()[0].img_url,
                'tag'               : item.product.tag.all()[0].color,
                'tag_text'          : item.product.productoption_set.all()[0].tag_text
            } for item in Cart.objects.select_related('product','tag').all()]
            return JsonResponse({ 'data': cart_list } ,status = 200)
        
        except  KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' }, status = 400)

    @login_decorator
    def patch(self,request):
        data = json.loads(request.body)
        try:
            product = Product.objects.prefetch_related('cart_set').get(id = data['product_id'])
            item    = Cart.objects.get(product_id = product.id)
            if item.amount >=  1:
                if data['changed_amount'] == 'plus':
                    item.amount +=1
                    item.save()
                    return HttpResponse( status = 200 )

                elif data['changed_amount'] == 'minus':
                    item.amount -=1
                    item.save()
                    return HttpResponse( status = 200 )
            return JsonResponse({ 'message' : 'INVALID_AMOUNT' }, status = 400)
        except  KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' }, status = 400)


    @login_decorator
    def delete(self,request):
        data = json.loads(request.body)
        try:
            item = Cart.objects.get(product_id = data['product_id'])
            item.delete()
            return HttpResponse(status = 200)
        
        except  KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' }, status=400)


