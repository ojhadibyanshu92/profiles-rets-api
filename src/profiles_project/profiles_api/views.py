from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken


from . import serializers
from . import models
from  . import permissions

class HelloAPIView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer


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

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""
        a_viewset =[
            "Uses action (list,crete,retrieve,update,partial_update)",
            "Automatically maps to the url using routers ",
            "Provides more functionality with less code."
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        """Create a hello message"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self,request,pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method':'Get'})

    def upadate(self,request,pk=None):
        """Handle an object update"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating part of object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handles removing an object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handels creating and Updating profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer

    def create(self,request):
        """use the ObtainAuthToken ApiView to validate and create a token"""
        return ObtainAuthToken().post(request)