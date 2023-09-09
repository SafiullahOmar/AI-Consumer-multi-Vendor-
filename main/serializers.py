from  rest_framework import serializers
from . import models


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields=['id','user','address']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ProductListSerializer(serializers.ModelSerializer):
    class Meta: 
        model=models.Product
        fields=['id','category','vendor','title','detail','price']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model=models.Product
        fields=['id','category','vendor','title','detail','price']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=['id','user','mobile']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=['id','user','mobile']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Order
        fields=['id','customer']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Order
        fields=['id','customer']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
