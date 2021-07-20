from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

class Login(View):
    def get(self , request):
        return render(request , 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        
        if customer:
            userpassword = Customer.objects.get(email = email)
            request.session['email'] = email
            request.session['customer'] = userpassword.id

            flag = check_password(password,userpassword.password)
            if flag:
                # request.session['customer_id'] = customer.id
                # request.session['customer_email'] = customer.email
                # request.session['customer_password'] = customer.password
                return redirect('homepage')
            else:
                return HttpResponse('Invalid Password')
        else:
            return HttpResponse('Invalid User!')
