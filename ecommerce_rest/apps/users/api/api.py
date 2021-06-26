#   rest_framework
from decimal import Context
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
#   Models
from apps.users.models import User
#   Serializers
from apps.users.api.serializers import UserSerializer, TestUserSerializer

@api_view(['GET','POST'])
def user_api_view(request):

    if request.method == 'GET':

        # queryset
        users = User.objects.all()
        users_serializer = UserSerializer(users,many = True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)


    
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        
        return Response(user_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request, pk=None):
    #   queryset
    user = User.objects.filter(id=pk).first()
    #   Validation
    if user:
        #   Retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        #   Update
        elif request.method == 'PUT':
            user_serializer = TestUserSerializer(user, data=request.data)

            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #   Delete
        elif request.method == 'DELETE':
            user.delete()
            return Response('Removed', status=status.HTTP_400_BAD_REQUEST)