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
class signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        if request.method == 'POST':
            print("hello hacker")
        print(request.method)
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        #validtion
        values={'first_name':first_name,
                'last_name':last_name,
                'phone':phone,
                'email':email
                
        }
        error_message=None
        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
        if not first_name:
            print("name ma problem che")
            error_message="please write name"
        if not last_name:
            error_message="please write last name"
        if not phone:
            error_message="please enter number"
        if not email:
            error_message="please enter email"
        if not password:
            error_message="please enter pasword"
        if not len(phone)==10:
            error_message="please enter 10 digits number"
        if customer.isExists():
            error_message="Email registered che bhai"
            # print(Customer.isExists())
        if not error_message:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('demo')
        
            
        else:
            data1={'error':error_message,
                  'values':values}

            return render(request,'signup.html',data1)
    
    
