from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.routers import Response
from rest_framework import status
# Create your views here.


class ExampleView(APIView):
    def get(self, request, *args, **kwargs):
        
        
        query_params = request.query_params
        
        name = query_params.get('name')
      
        
        return Response({"message": query_params}, status=status.HTTP_200_OK)


class Example2View(APIView):
    
    def get(self, request, *args, **kwargs):
        
        path_args = kwargs.get('pk')
        
        header = request.headers
        
        return Response({'message': path_args, 'headers': header}, status=status.HTTP_200_OK)