from django.urls import path,include

urlpatterns = [
    path('account',include('account.urls')),
    path('order',include('order.urls')),
    path('product',include('product.urls')),
    path('store',include('store.urls'))
]
