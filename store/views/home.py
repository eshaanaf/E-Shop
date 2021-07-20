from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

# Create your views here.

class Index(View):

    def post(self , request):
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')

        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product_id)
                    else:  
                        cart[product_id] = quantity-1
                else:
                    cart[product_id] = quantity+1
            else:
                cart[product_id]=1
        else:
            cart = {}
            cart[product_id]=1

        request.session['cart'] = cart
        return redirect('homepage')


    def get(self , request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_id(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request , 'index.html',data)




