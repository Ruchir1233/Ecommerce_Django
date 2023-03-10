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
from authentication.models.Product import Product
from . import demo


class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        print(products)
        return render(request,'cart.html',{'products':products})
    
    def post(self,request):
        demo.post(self,request)
    
    