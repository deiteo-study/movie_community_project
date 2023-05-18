from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def user(request):
    user=User.objects.filter(username=request.user)
    serializer=UserSerializer(data=user)
    return Response(serializer.data)

@api_view(['GET'])
def get_name(request,userId):
    user=get_object_or_404(User,id=userId)
    name=user.username
    return Response({'name':name})