from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied
class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method=="GET":
            return True
        else:
            if request.user.is_authenticated:
                return True
            else:
                raise PermissionDenied("Not Authorized!")
class VendorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.method=="GET":
            try:
                return obj.vender==request.user.vendor
            except:
                raise PermissionDenied("Not authorized!")
        return super().has_object_permission(request, view, obj)
class CartItemPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.method=="GET":
            try:
                return obj.customer==request.user.customer
            except:
                raise PermissionDenied("Not authorized!")
        return super().has_object_permission(request, view, obj)
class OrderModifyPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method=="GET" or not request.method=="GET":
            try:
                return obj.customer_user==request.user.customer
            except:
                raise PermissionDenied("Not authorized!")
        return super().has_object_permission(request, view, obj)
class ReviewPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ("GET","PUT","PATCH","DELETE"):
            try:
                return obj.review_user==request.user.customer
            except:
                raise PermissionDenied("Not Authorized!")
        return super().has_object_permission(request, view, obj)
    