from django.contrib import admin
from django.urls import path
from store.views.login import  Login
from store.views.signup import  signup
from store.views.home import Index
from store.views.logout import  logout
from store.views.cart import  Cart
from store.views.checkout import  CheckOut
from store.views.orders import  OrderView

urlpatterns = [
    path('',Index.as_view() , name= 'homepage'),
    path('signup' ,signup , name='signup'),
    path('login' ,Login.as_view() , name='login'),
    path('logout' ,logout , name='logout'),
    path('cart' ,Cart.as_view() , name='cart'),
    path('check-out' , CheckOut.as_view(), name='checkout'),
    path('orders' , OrderView.as_view(), name='orders'),
]
