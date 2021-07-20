from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request,'cart.html' , {'products': products})