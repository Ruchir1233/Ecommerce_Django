from email.policy import default
from django.db import models
from picklefield import PickledObjectField
from numpy import True_, true_divide
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15,null=True)
    email=models.EmailField()
    password=models.CharField(max_length=20) 
    # user_cart_value=PickledObjectField(default="0")
    
    def register(self):
        self.save()
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    
    def get_user_cart(email):
        try:
            return Customer.objects.filter(email='email').values('user_cart_value')
        except:
            print("NO CART VALUE FOUND")