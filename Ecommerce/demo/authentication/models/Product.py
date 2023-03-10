from django.db import models
from .categories import Category
class Product(models.Model):
    p_name=models.CharField(max_length=50)
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to="images1/")
    
    def __str__(self):
        return self.p_name
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
           return Product.get_all_products()
       
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)