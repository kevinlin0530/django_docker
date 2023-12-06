from django.shortcuts import render
from .models import Store
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView , CreateView
from django.utils.translation import gettext_lazy as _
from rest_framework import generics
from .serializer import StoreSerializer
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

class Storeview(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    def create(self,request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            name = request.data.get('name')
            location = request.data.get('location')
            queryset = Store.objects.filter(name = name ,location=location)
            if queryset.exists():
                result = {
                    'failed':'已有相同商店在相同位置註冊'
                }
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                result = {
                    'success':'商店建立完成',
                    'data':serializer.data
                    }
                return Response(result,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,*args, **kwargs):
        name_pk = kwargs.get('pk')
        queryset = Store.objects.get(id=name_pk)
        serializer = StoreSerializer(queryset,data = request.data,partial=True)
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
        
    def list(self,request):
        location = request.data.get('location')
        name = request.data.get('name')
        if location:
            queryset = Store.objects.filter(location=location)
            serializer = StoreSerializer(queryset,many=True)
            if queryset:
                result = {
                    'success':'以下是搜索結果',
                    'data':serializer.data
                }
                return Response(result,status=status.HTTP_200_OK)
            else:
                result = {
                    "failed":'目前無資料',
                }
                return Response(result,status=status.HTTP_404_NOT_FOUND)
        elif name:
            queryset = Store.objects.filter(name=name)
            serializer = StoreSerializer(queryset,many=True)
            if queryset:
                result = {
                    'success':'以下是搜索結果',
                    'data':serializer.data
                }
                return Response(result,status=status.HTTP_200_OK)
            else:
                result = {
                    "failed":'目前無資料',
                }
                return Response(result,status=status.HTTP_404_NOT_FOUND)
        else:
            result = {
                'failed':'請輸入店名或地址'
            }
            return Response(result,status=status.HTTP_400_BAD_REQUEST)