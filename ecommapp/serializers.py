from rest_framework import serializers
from .models import Product,CartItem,Review,Order,Customer,Vendor
class CustomerSerializer(serializers.ModelSerializer):
    cart=serializers.StringRelatedField(many=True)
    class Meta:
        model=Customer
        fields="__all__"
    def validate_phone(self,obj):
        if not len(obj)==10:
            raise serializers.ValidationError("Phone number should be 10 digits!")
        else:
            return obj
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields="__all__"
class ProductSerializer(serializers.ModelSerializer):
    review=serializers.StringRelatedField(many=True)
    vender=VendorSerializer()
    class Meta:
        model=Product
        fields="__all__"
class CartItemSerializer(serializers.ModelSerializer):
    products=serializers.StringRelatedField()
    class Meta:
        model=CartItem
        fields="__all__"
    def validate(self,data):
        request=self.context["request"]
        if request.method!="PATCH":
            customer=data["customer"]
            products=data["products"]
            if CartItem.objects.filter(customer=customer,products=products).exists():
                raise serializers.ValidationError("Cart already exists!")
            else:
                return data
        else:
            return data
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"
class ReviewSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Review
        fields="__all__"
    def validate(self,data):
        request=self.context["request"]
        product=data["product"]
        review_user=data["review_user"]
        if not hasattr(request.user,"customer"):
            raise serializers.ValidationError("Not Authorized!")
        else:
            order_data=Order.objects.filter(status="Success",customer_user=request.user.customer,products=product).exists()
            if order_data:
                return data
            else:
                raise serializers.ValidationError("Not Authorized")



    