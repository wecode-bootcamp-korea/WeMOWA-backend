import json
import bcrypt
import jwt

from django.views import View
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.db import IntegrityError

from my_settings import SECRET_KEY
from .models import User, Prefix, UserWishlist
from .utils import login_decorator


class SignUpView(View):
    def post(self,request):
        try:
            data = json.loads(request.body)
            password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt())
            crypted = password.decode('utf-8')
            User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                email = data['email'],
                password = crypted,
                country = data['country'],
                prefix = Prefix.objects.get(name = data['prefix'])
            )
            return HttpResponse(status = 200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'},status = 400)
        except IntegrityError:
            return JsonResponse({'message':'DUPLICATE_ENTRIES'},status = 400)

class SignInView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])
                if bcrypt.checkpw(data['password'].encode('utf-8'),user.password.encode('utf-8')):
                    token = jwt.encode({'email':data['email']}, SECRET_KEY['SECRET_KEY'], algorithm = 'HS256')
                    token = token.decode('utf-8')
                    return JsonResponse({'token':token}, status = 200)
                else:
                    return JsonResponse({'message':'INVALID_USER'}, status = 401)
            else:
                return JsonResponse({'message':'INVALID_USER'}, status = 401)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)

class WishListView(View):
    @login_decorator
    def post(self,request):
        try:
            if request.user != '':
                user = request.user
                product_id = request.GET.get('product_id',None)
                if UserWishlist.objects.filter(product_id = product_id, user_id = user.id).exists():
                        return JsonResponse({'message':'PRODUCT ALREADY IN THE WISHLIST'}, status = 400)
                else:
                    UserWishlist.objects.create(
                        user_id = user.id,
                        product_id = product_id
                    )
            return HttpResponse(status = 200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)

    @login_decorator
    def get(self,request):
        try:
            result = []
            if request.user != '':
                user = User.objects.prefetch_related('userwishlist_set').get(id = request.user.id)
                product_list = user.wishlist.select_related('collection').all()
                for product in product_list:
                    product_info = {}
                    product_info['collection'] = product.collection.name
                    product_info['name'] = product.name
                    product_info['price'] = product.price
                    product_info['image'] = product.image_set.all()[0].img_url
                    result.append(product_info)
            return JsonResponse({'data':result},status = 200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)

    @login_decorator
    def delete(self,request):
        try:
            if request.user != '':
                product_id = request.GET.get('product_id',None)
                item = UserWishlist.objects.get(product_id = product_id, user_id = request.user.id)
                item.delete()
                return HttpResponse(status = 200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)
        except UserWishlist.DoesNotExist:
            return JsonResponse({'message':'WISHLIST DOES NOT EXIST'}, status = 400)


