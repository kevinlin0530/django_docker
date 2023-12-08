from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from product.models import Product
from store.models import Store
from django.core.validators import RegexValidator
from django.db.models import Sum, Count

class User(models.Model):
    email = models.EmailField(unique=True,null=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    id_number = models.CharField(max_length=10,null=False,
            validators=[
            RegexValidator(
                regex=r'^[A-Z][1-2]\d{8}$',
                message='請輸入有效的身分證號碼',
                code='invalid_id_number'
            )
        ])
    birthday = models.DateField()
    phone_number = models.CharField(max_length=20, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    purchases = models.ManyToManyField('Purchase', related_name='name', blank=True)
    def __str__(self):
        return self.name

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['name', 'gender', 'birthday', 'phone_number', 'created_at','update_time', 'is_email_verified', 'is_phone_verified']
#     search_fields = ('name','gender',)
#     ordering = ('name',)

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_purchases',default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_purchases', default=None)
    store_name = models.ForeignKey(Store, on_delete=models.CASCADE,related_name='store_purchases', default=None)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=None)

    def __str__(self):
        return f"{self.product.item}"
    
class PurchaseInline(admin.TabularInline):  # 或者 admin.StackedInline，視覺風格不同
    model = Purchase
    extra = 0  # 控制要顯示的空白表單數量
    show_change_link = True  # 點擊每行可以進入該對應物件的編輯頁面
    can_delete = True  # 顯示刪除按鈕
    fields = ['product', 'store_name', 'price']  # 控制展示的字段


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'birthday', 'phone_number', 'created_at', 'update_time', 'is_email_verified', 'is_phone_verified']
    search_fields = ('name', 'gender',)
    ordering = ('name',)
    inlines = [PurchaseInline]  # 將 PurchaseInline 加入這裡
