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
    product_rating=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta: 
        model=models.Product
        fields=['id','category','title','detail','price','product_rating']
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
        model=models.OrderItems
        fields=['id','order','product']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CustomerAddres
        fields=['id','customer','address','default_address']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductRating
        fields=['id','customer','product','rating','reviews','add_time']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductCategory
        fields=['id','detail','title']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ProductCategory
        fields=['id','title','detail']
        depth=1
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)