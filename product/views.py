from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.http import Http404 # type: ignore
from drf_yasg.utils import swagger_auto_schema # type: ignore
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(APIView):
    def get(self,request):
        products = Product.objects.filter(is_active=True)
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=ProductSerializer)  
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailAPIView(APIView):
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk,is_active=True)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ProductSerializer)  
    def put(self,request,pk):
        product = self.get_object(pk)
        serializer  = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=ProductSerializer)  
    def patch(self,request,pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        product = self.get_object(pk)
        product.is_active=False
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)