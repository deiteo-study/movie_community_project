from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from movies.serializers import ReviewSerializer
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
# @api_view(['GET'])
# def user(request):
#     user=User.objects.filter(username=request.user)
#     serializer=UserSerializer(data=user)
#     return Response(serializer.data)

@api_view(['GET'])
def get_name(request,userId):
    user=get_object_or_404(User,id=userId)
    name=user.username
    return Response({'name':name})

@api_view(['POST'])
def password_check(request):
    print(request.user)
    print(request.data['password'])
    return Response('d')

@api_view(['GET'])
def delete(request):
    user=get_object_or_404(User, username=request.user)
    user.delete()
    return Response('delete')

@api_view(['GET'])
def get_user(request,username):
    try:
        user=User.objects.get(username=username)
    except:
        return Response(False)
    if user==request.user:
        me=True
    else:
        me=False
    serializer=UserSerializer(user)
    return Response({'data':serializer.data,'me':me})