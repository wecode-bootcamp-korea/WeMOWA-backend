import json
from django.shortcuts import render
from django.views import  View
from django.http import HttpResponse, JsonResponse
from .models import Cart, Order, OrderStatus
from product.models import Product
from account.utils import login_decorator


class CartView(View):
   @login_decorator
   def post(self,request):
        data = json.loads(request.body)
        try:
           cart_item =  Product.objects.select_related('category','collection','texture','stock_status').prefetch_related('tag','handle','wheel').get(product_number = data['product_number'])

           Order.objects.create(
               user_id = request.user.id,
               order_status_id = 1
           )
           Cart.objects.create(
               product_id  = cart_item.id,
               amount      = data['amount']
           )
           return HttpResponse( status = 200 )
        except KeyError:
            return JsonResponse({ 'message' : 'INVALID_KEYS' }, status = 400)
