from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class HelloAPIView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializers


    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'It is similar to the conditional django view',
            'Gives you the must control over your logic',
            'It mapped manually to urls'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer = serializers.HelloSerializers(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handels the updating an object"""
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """patch request ,only updates fields provided in the request"""
        return Response({'method':'patch'})

    def delete(self,request,pk=None):
        """Deletes the object"""
        return Response({'method':'delete'})
