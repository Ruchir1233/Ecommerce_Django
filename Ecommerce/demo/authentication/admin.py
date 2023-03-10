from django.contrib import admin


from authentication.models.Product import Product
from authentication.models.Product import Category
from authentication.models.customer import Customer
from authentication.models.orders import Order

class AdminProduct (admin.ModelAdmin) :
    list_display = ['p_name', 'price', 'category' ]
admin.site.register(Product, AdminProduct)



class AdminCategory (admin.ModelAdmin) :
    list_display = ['name']
# Register your models here.
# admin.site.register(Product)
admin.site.register(Category,AdminCategory )
admin.site.register(Customer)
admin.site.register(Order)