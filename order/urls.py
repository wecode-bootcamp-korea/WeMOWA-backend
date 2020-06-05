from django.urls import path
from .views import CartView, OrderView

urlpatterns = [
    path('',CartView.as_view()),
    path('/payment', OrderView.as_view())
]
