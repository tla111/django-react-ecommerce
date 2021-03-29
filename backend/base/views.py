from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Product
from base.products import products
from base.serializers import ProductSerializer

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
  routes = [
    '/api/products/',
  ]
  return Response(routes)


@api_view(['GET'])
def getProducts(request):
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def getProduct(request, pk):
  product = Product.objects.get(_id=pk)
  serializer = ProductSerializer(product, many=False)
  return JsonResponse(serializer.data, safe=False)