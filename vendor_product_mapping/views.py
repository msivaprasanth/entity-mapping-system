from rest_framework.views import APIView  # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.http import Http404  # type: ignore
from drf_yasg.utils import swagger_auto_schema # type: ignore
from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer

class VendorProductMappingListCreateAPIView(APIView):
    def get(self,request):
        queryset = VendorProductMapping.objects.filter(is_active=True)
        vendor_id = request.query_params.get('vendor_id')
        if vendor_id:
            queryset = queryset.filter(vendor_id=vendor_id)
        serializer = VendorProductMappingSerializer(queryset,many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=VendorProductMappingSerializer) 
    def post(self,request):
        serializer = VendorProductMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class VendorProductMappingDetailAPIView(APIView):
    def get_object(self,pk):
        try:
            return VendorProductMapping.objects.get(pk=pk)
        except VendorProductMapping.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        mapping =  self.get_object(pk)
        serializer =  VendorProductMappingSerializer(mapping)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=VendorProductMappingSerializer) 
    def put(self,request,pk):
        mapping =  self.get_object(pk)
        serializer =  VendorProductMappingSerializer(mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=VendorProductMappingSerializer) 
    def patch(self,request,pk):
        mapping = self.get_object(pk)
        serializer = VendorProductMappingSerializer(mapping,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        mapping =  self.get_object(pk)
        mapping.is_active=False
        mapping.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
