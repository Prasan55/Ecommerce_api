from django.contrib import admin
from .models import CartItem,Product,Order,Review,Vendor,Customer
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Vendor)
admin.site.register(Customer)
# Register your models here.
