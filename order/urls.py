from django.urls import path
from .views import CartView

urlpattern = [
    path('',CartView.as_view()),

] 
