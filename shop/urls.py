"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from product.views import ProductView
from user.views import UserViews,PurchaseViews
from store.views import Storeview


product_router = DefaultRouter()
product_router.register(r'',ProductView)

user_router = DefaultRouter()
user_router.register(r'',UserViews)

store_router = DefaultRouter()
store_router.register(r'',Storeview)

purchase_router = DefaultRouter()
purchase_router.register(r'',PurchaseViews)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registration/',include(user_router.urls)),
    path('api/storesignup/',include(store_router.urls)),
    path('api/product/',include(product_router.urls)),
    path('api/purchase/',include(purchase_router.urls))
]
