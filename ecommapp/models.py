from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    customer_id=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
class Vendor(models.Model):
    vendor_id=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    vender=models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    category=models.CharField(max_length=100)
    manufactured_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product_name
class CartItem(models.Model):
    cartuser_id=models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,related_name="cart")
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
class Order(models.Model):
    status=models.CharField(max_length=10,choices=[("Success","Success"),("Failed","Failed")])
    total_price=models.IntegerField(default=0)
    order_date=models.DateTimeField(auto_now_add=True)
    customer_user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,related_name="order_placed")
    products=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="review")
    review_user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    rating=models.IntegerField(choices=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)])

# Create your models here.
