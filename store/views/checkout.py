from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from django.views import View

class CheckOut(View):
    def post(self , request):
        address = request.POST.get('address')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address , customer , products)

        for product in products:
            order= Order( customer = Customer(id =  customer) , product = Product(id = product.id) , price = product.price , quantity = cart.get(str(product.id)) , address = address)
            order.placeOrder()
        request.session['cart'] = {}
        return redirect('cart')
