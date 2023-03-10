from django.views import View
from cProfile import Profile
from distutils.log import error
import email
from genericpath import exists
from multiprocessing import context
from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from requests import post
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.shortcuts import redirect
import random
from authentication.models.Product import Product
from authentication.models.categories import Category
from authentication.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from authentication.function import function

class login(View):
    def get(self,request):
      
        return render(request,'login.html',{'error_message':error})
    def post(self,request):
        print("hi")
        email=request.POST.get('email')
        request.session['email']=email
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)

        error_message=None
        if customer:
            email=request.session.get('email')
            print(email)
            # a=Customer.objects.all()[0]['email']
            # a = Customer.objects.filter(email=email).values('user_cart_value')
            # print("aaj joie che ne?",a)
            # print("MAI A CHU GUYS BRO",email)
            # for i in a:
                # user_cart=i['user_cart_value']['email']
            flag=check_password(password,customer.password)
            print(flag)
            if flag:
                request.session['email']=email
                print(email)
                request.session['customer']=customer.id
                return redirect('demo')
            else:
                error_message="password khoto che dost"
        else:
            error_message="invalid email"
        # request.session['cart']=user_cart
        
        # print(email)
        
        # user_login_cart=dict()
        # user_login_cart[email]=cart
        # a.user_cart_value=user_login_cart
        # print("done ruchir")
        # cart=request.session['cart']
        # print("login.py ni cart che aa",cart)
        return render(request,'login.html',{'error':error_message})
    
def logout(request):
    request.session.clear()
    return redirect('login')