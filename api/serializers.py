from dataclasses import fields
from rest_framework import serializers

# from rest_framework_json_api import serializers
from store.models import Product


# class ProductSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'price', 'stock')

