import json

from django.shortcuts import render
from django.views import  View
from django.http import HttpResponse, JsonResponse

from .models import Cart, Order, OrderStatus
from product.models import Product, ProductOption, Tag
from account.utils import login_decorator
from account.models import User 

class CartView(View):
    @login_decorator
    def post(self,request):
        try:
            data = json.loads(request.body)
            user = request.user
            product_id = data['product_id']
            tag = data['tag']
            amount = data['amount']
            tag_text = data['tag_text']
            cart_item =  Product.objects.get(id = product_id)
            if "tag" in data:
                ProductOption.objects.create(
                    product_id  = product_id,
                    tag         = Tag.objects.get(color = tag),
                    tag_text    = tag_text
                )
            
            if not Order.objects.filter(user = user, order_status__name = 'pending').exists():
                order_item  = Order.objects.create(
                    user_id = user.id,
                    order_status = OrderStatus.objects.get(name = "pending")
                )
            
            if Cart.objects.filter(order__user = user, product_id = product_id).exists():
                item = Cart.objects.get(product_id=product_id)
                item.amount += 1
                item.save()
            
            else:
                Cart.objects.create(
                    product         = cart_item,
                    amount          = amount,
                    tag             = Tag.objects.get(color = tag.upper()),
                    order           = Order.objects.get(user = user, order_status__name ='pending')
                    )
            return HttpResponse( status = 200 )

        except KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' }, status = 400)

    @login_decorator
    def get(self,request):
        try:
            user = request.user
            items = Cart.objects.select_related('product','tag','order').filter(order__user = user)
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
            } for item in items]
            return JsonResponse({ 'data': cart_list } ,status = 200)
        
        except  KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' }, status = 400)

    @login_decorator
    def patch(self,request):
        data = json.loads(request.body)
        try:
            user = request.user
            item    = Cart.objects.get(order__user = user, product_id = data['product_id'])
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
            user = request.user
            item = Cart.objects.get(order__user = user, product_id = data['product_id'])
            item.delete()
            return HttpResponse(status = 200)
        
        except  KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' }, status=400)

class OrderView(View):
    @login_decorator
    def post(self,request):
        data = json.loads(request.body)
        user = request.user
        try:
            if data:
                order = Order.objects.get(user = user, order_status__name = 'pending')
                order.order_status_id = 2
                order.save()
                return HttpResponse(status = 200)
            
            return JsonResponse({ 'message' : 'INVALID_DATA' }, status = 400)
        
        except KeyError:
             return JsonResponse({ 'message' : 'INVALID_KEY' }, status = 400)

