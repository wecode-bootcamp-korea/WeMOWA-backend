import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.db.models import Q

from .models import Store

class StoreListView(View):
    def get(self,request):
        result = []
        search = request.GET.get('search', None)
        store_list = Store.objects.prefetch_related('storestoretype_set').all()
        if search:
            store_list = store_list.filter(Q(city__istartswith = search) | Q(name__icontains = search) | Q(address__icontains = search))
        for store in store_list:
            store_info = {}
            store_info['name'] = store.name
            store_info['city'] = store.city
            store_info['postal_code'] = store.postal_code
            store_info['address'] = store.address
            store_info['store_type'] = [store_type.name for store_type in store.store_type.all()]
            store_info['lat'] = store.lat
            store_info['lng'] = store.lng
            store_info['image'] = store.img_url
            result.append(store_info)
        print(len(result), len(store_list.values()))
        return JsonResponse({'data':result}, status = 200)

