from django.shortcuts import render
from . import models 
from . import serializers
from rest_framework import generics ,permissions
# Create your views here.

class VendorList(generics.ListCreateAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer
    #permission_classes=[permissions.IsAuthenticated]

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorDetailSerializer
    #permission_classes=[permissions.IsAuthenticated]        
class ProductList(generics.ListCreateAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductListSerializer
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductDetailSerializer


class CustomerList(generics.ListCreateAPIView):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.CustomerSerializer
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.CustomerDetailSerializer

class OrderList(generics.ListCreateAPIView):
    queryset=models.Order.objects.all()
    serializer_class=serializers.OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Order.objects.all()
    serializer_class=serializers.OrderDetailSerializer