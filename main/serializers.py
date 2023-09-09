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

