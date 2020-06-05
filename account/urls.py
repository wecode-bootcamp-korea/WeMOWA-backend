from django.urls import path
from .views import SignUpView,SignInView,WishListView

urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignInView.as_view()),
    path('/wishlist', WishListView.as_view())
]
