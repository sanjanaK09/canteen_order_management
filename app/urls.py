from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_item, name='remove'),
    path('checkout/', views.checkout, name='checkout'),
    path('increase/<int:id>/', views.increase_qty, name='increase'),
    path('decrease/<int:id>/', views.decrease_qty, name='decrease'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),

    path('login/', views.login, name='login'),
    path('verify/', views.verify_otp, name='verify_otp'),
]