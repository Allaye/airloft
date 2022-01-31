from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from rest_framework import (response, status, permissions)
from account.serializers import RegisterApiViewSerializer, LoginApiViewSerializer

# Create your api views here.
class RegisterApiView(GenericAPIView):
    '''
    Create a new project object, and return the created object.
    permission_classes = "IsAuthenticated" :user is logged in , "IsAdminUser" : user is admin
    Post: /api/register
    {
    "username": "ab",
    "email": "ab@email.com",
    "password": "ab@email.com"
    }

    response:
    {
    "id": 1,
    "username": "ab",
    "email": "ab@email.com",
    "is_staff": false
    }
    '''
    authentication_classes = []
    serializer_class = RegisterApiViewSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
