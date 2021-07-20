from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

def signup(request):
    if(request.method == 'GET'):
        return render(request , 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')

        customer = Customer(first_name = first_name , last_name = last_name , email = email , password = password)
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('homepage')
