from django.shortcuts import render
from rest_framework import generics
from .models import Product,Order,CartItem,Review,Customer,Vendor
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
from .permissions import CustomPermission,VendorPermission,CartItemPermission,OrderModifyPermission,ReviewPermission
from rest_framework.exceptions import PermissionDenied
from .serializers import ProductSerializer,OrderSerializer,CartItemSerializer,ReviewSerializer,CustomerSerializer,VendorSerializer
from django_filters.rest_framework import DjangoFilterBackend

# All the classes use JWT Authentication

# Anyone can view customers but only admin users can add customers
class CustomerList(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes=[CustomPermission]

# Only admin users are allowed to modify customers
class CustomerModify(generics.RetrieveUpdateDestroyAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes=[CustomPermission]

# Anyone can view vendor list but only admin users can add vendors
class VendorList(generics.ListCreateAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer
    permission_classes=[CustomPermission]

# Only admin users can modify vendors
class VendorModify(generics.RetrieveUpdateDestroyAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer
    permission_classes=[CustomPermission]

# Only vendors and admin users can add products
class ProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["product_name","category"]
    def get_permissions(self):
        if self.request.method=="POST":
            if hasattr(self.request.user,"vendor"):
                return [IsAuthenticated()]
            elif not hasattr(self.request.user,"vendor"):
                return [IsAdminUser()]
            else:
                raise PermissionDenied("Not authorized!")
        else:
            return [AllowAny()]
    
# vendors can modify only their own products
class ProductModify(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[VendorPermission]

# Only customers and admin users can add cartitems
class CartItemList(generics.ListCreateAPIView):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer
    def get_queryset(self):
        return CartItem.objects.filter(customer=self.request.user.customer)
    def get_permissions(self):
        if self.request.method=="POST":
            if hasattr(self.request.user,"customer"):
                return [IsAuthenticated()]
            elif not hasattr(self.request.user,"customer"):
                return [IsAdminUser()]
            else:
                raise PermissionDenied("Not authorized!")
        return super().get_permissions()
    
# customers can modify only their own products
class CartItemModify(generics.RetrieveUpdateDestroyAPIView):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer
    permission_classes=[CartItemPermission]

# Only customers are allowed to create orders and they can only view their own orders
class OrderList(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    def get_queryset(self):
        try:
            return Order.objects.filter(customer_user=self.request.user.customer)
        except:
            raise PermissionDenied("Not Authorized!")
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        else:
            if hasattr(self.request.user,"customer"):
                return [IsAuthenticated()]
        return super().get_permissions()
    
# customers can modify only their own orders
class OrderModify(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[OrderModifyPermission]

# Anyone can view reviews and only customers can post review to their own products which has order status success
class ReviewList(generics.ListCreateAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["rating"]
    def get_permissions(self):
        if self.request.method=="GET":
            return [AllowAny()]
        return super().get_permissions()
    
# customers can modify only their own reviews
class ReviewModify(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[ReviewPermission]

# Create your views here.
