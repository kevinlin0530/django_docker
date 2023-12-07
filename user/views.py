from django.shortcuts import render
from .models import User,Purchase
from product.models import Product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView , CreateView
from django.utils.translation import gettext_lazy as _
from rest_framework import generics
from .serializer import UserSerializer,PurchaseSerializer
from rest_framework.permissions import AllowAny,IsAdminUser , IsAuthenticated
from django.db.models.fields.files import ImageFieldFile
from decimal import Decimal
from rest_framework import viewsets , status
from datetime import date, datetime
import json
from rest_framework.decorators import api_view, permission_classes ,action
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication ,TokenAuthentication
from rest_framework.parsers import JSONParser ,FormParser,MultiPartParser
from django.db.models import Q
# Create your views here.

class UserViews(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    def create(self,request):
        serializer = UserSerializer(data = request.POST)
        if serializer.is_valid():
            email = request.data.get('email')
            phone_number = request.data.get('phone_number')
            id_number = request.data.get('id_number')
            email_queryset = User.objects.filter(email=email)
            phone_queryset = User.objects.filter(phone_number=phone_number)
            id_number_queryset = User.objects.filter(id_number=id_number)
            if email_queryset.exists():
                result = {"error":"電子信箱已註冊"}
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
            elif id_number_queryset.exists():
                result = {"error":"身分證已註冊"}
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
            elif phone_queryset.exists():
                result = {"error":"電話已註冊"}
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                result = {
                    'success':"註冊成功",
                    'data':serializer.data
                        }
                return Response(result , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,*args, **kwargs):
        user_pk = kwargs.get('pk')
        queryset = User.objects.get(id=user_pk)
        serializer = UserSerializer(queryset,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            result = {
                'success':"資料更新成功",
                'data':serializer.data
                }
            return Response(result, status=status.HTTP_200_OK)
        else:
            result = {"result":"更新失敗"}
            return Response(result,status=status.HTTP_400_BAD_REQUEST)

class PurchaseViews(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class =PurchaseSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    def create(self,request):
        serializer = PurchaseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            result = {
                'success':'購買完成',
                'data':serializer.data
            }
            return Response(result,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)