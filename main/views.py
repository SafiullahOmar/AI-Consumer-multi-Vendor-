from django.shortcuts import render
from . import models 
from . import serializers
from rest_framework import generics ,permissions , viewsets
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
    queryset=models.OrderItems.objects.all()
    serializer_class=serializers.OrderDetailSerializer

    def get_queryset(self):
        order_id=self.kwargs['pk']
        order=models.Order.objects.get(id=order_id)
        order_items=models.OrderItems.objects.filter(order=order)

        return order_items
    
class CustomerAddress(viewsets.ModelViewSet):
    serializer_class=serializers.CustomerAddressSerializer
    queryset=models.CustomerAddres.objects.all()

class ProductRatingViewset(viewsets.ModelViewSet):
    serializer_class=serializers.ProductRatingSerializer
    queryset=models.ProductRating.objects.all()

class CategoryList(generics.ListCreateAPIView):
    queryset=models.ProductCategory.objects.all()
    serializer_class=serializers.CategorySerializer
    #permission_classes=[permissions.IsAuthenticated]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.ProductCategory.objects.all()
    serializer_class=serializers.CategoryDetailSerializer