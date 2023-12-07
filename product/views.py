from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView , CreateView
from django.utils.translation import gettext_lazy as _
from rest_framework import generics
from .serializer import ProductSerializer
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

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            result = {
                'success':'產品上架成功',
                'data':serializer.data
            }
            return Response(result,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
