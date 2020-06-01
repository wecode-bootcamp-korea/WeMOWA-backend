import json
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import User
from .models import Prefix
from django.shortcuts import render
from django.db import IntegrityError
import bcrypt
import jwt
from my_settings import SECRET_KEY

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
                return JsonResponsse({'message':'INVALID_USER'}, status = 401)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)



