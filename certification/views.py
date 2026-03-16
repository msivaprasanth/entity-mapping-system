from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response  # type: ignore
from rest_framework import status  # type: ignore
from django.http import Http404 # type: ignore
from drf_yasg.utils import swagger_auto_schema # type: ignore
from .models import Certification
from .serializers import CertificationSerializer

class CertificationListCreateAPIView(APIView):
    def get(self,request):
        certifications = Certification.objects.filter(is_active=True)
        serializer = CertificationSerializer(certifications,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=CertificationSerializer) 
    def post(self,request):
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CertificationDetailAPIView(APIView):
    def get_object(self,pk):
        try:
            return Certification.objects.get(pk=pk,is_active=True)
        except Certification.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=CertificationSerializer) 
    def put(self,request,pk):
        certification = self.get_object(pk)
        serializer  = CertificationSerializer(certification,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=CertificationSerializer) 
    def patch(self,request,pk):
        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        certification = self.get_object(pk)
        certification.is_active=False
        certification.save()
        return Response(status=status.HTTP_204_NO_CONTENT)