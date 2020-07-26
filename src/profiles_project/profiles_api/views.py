from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API view"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'It is similar to the conditional django view',
            'Gives you the must control over your logic',
            'It mapped manually to urls'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
