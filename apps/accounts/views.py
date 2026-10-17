from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.routers import Response
from rest_framework import status
# Create your views here.


class ExampleView(APIView):
    def get(self, request, *args, **kwargs):
        
        
        query_params = request.query_params
        
        name = query_params.get('name')
        fullname = query_params.get('fullname')
        
        return Response({"message": f"Hello, {name}!"}, status=status.HTTP_200_OK)