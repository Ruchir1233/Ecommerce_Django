from cProfile import Profile
# from curses import pair_number
from distutils.log import error
import email
from genericpath import exists
from multiprocessing import context
from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from numpy import product
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
from authentication.templatetags import cart
from authentication.function import function
class demo(View):
      
    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session.cart ={}
        categories=Category.objects.all()
        category_ID=request.GET.get('category')
        if category_ID:
            products=Product.get_all_products_by_category_id(category_ID)
        else:
            products=Product.get_all_products
        data={}
        data['products']=products
        data['categories']=categories
        # print("bye",request.session['email'])
        print(cart)
        return render(request,'index.html',data,)
    
    # def post(self, request):
    #     data= request.POST.dict()
    #     remove=data.get("remove")
    #     product = request.POST.get('product')
    #     email=request.session['email']
    #     # print("EMAIL CHE AA JOV",email)
    #     # cart=user_cart
    #     # cart = request.session.get('cart')
    #     print("EMAIL CHE AA   ",email)
    #     print("gfgcdfghjhgfdsfgh",Customer.objects.filter(email='email').values('first_name'))
    #     # if Customer.objects.filter(email='email').values('id'):
    #     # if 1==1:
    #     #     a = Customer.objects.filter(email='email').values('user_cart_value')
    #     #     a=Customer.get_user_cart(email)
    #     #     print("MAI A CHU GUYS BRO",a)
    #     #     user_cart=list()
    #     #     for i in a:
    #     #         user_cart=i['user_cart_value']['email']
    #     #     print("user_cart",user_cart)
    #     #     request.session['cart']=user_cart
    #     #     print("aa cart",request.session['cart'])
    
    #     if request.session.get('cart') is None:
    #         cart={}
    #         cart[product]=0
    #         if  cart[product]==0:
    #             cart[product]=1
    #     else:
    #         print("remo",remove)
    #         try:
    #             if remove:
    #                 cart[product]-=1
    #                 if cart[product]<=0:
    #                     cart.pop(product)
    #                 print("remove ma aavya che")
                    
    #             else:
    #                 if cart[product]:
    #                     print("hello i am error")
    #                     if cart[product]==0:
    #                         cart[product]=1
    #                     if cart[product]>=1:
    #                         cart[product]+=1  
    #         except KeyError :
    #             cart[product]=0
    #             if cart[product]==0:
    #                 cart[product]=1
    #             # if cart[product]>=1:
    #             else:
    #                 cart[product]+=1
        
    #     # a=Customer.objects.get(email='email')
    #     # a=Customer.get_customer_by_email(email)
        
    #     # print("MAI A CHU GUYS BRO",a)
    #     # # print(email)
        
    #     # user_login_cart=dict()
    #     # # user_login_cart[email]=cart
    #     # a.user_cart_value={'email':cart}
    #     # a.save()
    #     # print("done ruchir")
    #     # n = Customer.objects.filter(email='email').values('user_cart_value')
    #     # print("AAA CUSTOMER ID CHEHHHH",n)
    #     request.session['cart'] = cart
    #     return redirect('demo')
    
        

# def demo(request):
    
    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        email = request.session.get('email')
        # a=Customer.objects.filter(email='email').update(user_cart_value='')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('demo')