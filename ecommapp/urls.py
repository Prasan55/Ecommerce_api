from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
urlpatterns = [
    path('',views.APIRoot.as_view(),name="api-root"),
    path('productlist/',views.ProductList.as_view()),
    path('productmodify/<int:pk>',views.ProductModify.as_view()),
    path('cartitemlist/',views.CartItemList.as_view()),
    path('cartitemmodify/<int:pk>',views.CartItemModify.as_view()),
    path('orderlist/',views.OrderList.as_view()),
    path('ordermodify/<int:pk>',views.OrderModify.as_view()),
    path('reviewlist/',views.ReviewList.as_view()),
    path('reviewmodify/<int:pk>',views.ReviewModify.as_view()),
    path('customerlist/',views.CustomerList.as_view()),
    path('customermodify/<int:pk>',views.CustomerModify.as_view()),
    path('vendorlist/',views.VendorList.as_view()),
    path('vendormodify/<int:pk>',views.VendorModify.as_view()),
    path('token/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('verifytoken/',TokenVerifyView.as_view())
]