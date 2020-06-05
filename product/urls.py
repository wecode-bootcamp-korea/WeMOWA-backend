from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('/<int:category_id>', ProductListView.as_view()),
    path('', ProductDetailView.as_view())
]
