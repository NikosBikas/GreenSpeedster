from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.response import Response
from .serializers import *
from store.models import *
# from rest_framework import viewsets
from rest_framework.decorators import api_view

# class ProductViewSet(viewsets.ModelViewSet):  
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#     search_fields = ['product_name','description', 'price', 'stock']


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)

