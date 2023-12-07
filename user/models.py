from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from product.models import Product
from store.models import Store
from django.core.validators import RegexValidator

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

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'birthday', 'phone_number', 'created_at','update_time', 'is_email_verified', 'is_phone_verified']
    search_fields = ('name','gender',)
    ordering = ('name',)
    filter_horizontal = ('purchases',)

    # def get_total_spent(self, obj):
    #     return obj.total_spent

    # get_total_spent.short_description = '總消費'

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_purchases',default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_purchases', default=None)
    store_name = models.ForeignKey(Store, on_delete=models.CASCADE,related_name='store_purchases', default=None)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=None)

    def __str__(self):
        return f"{self.product.item} - {self.price} - {self.purchase_date} - {self.store_name.name}"
    
    # def purchases_display(self, obj):
    #     return ", ".join([purchase.product_name for purchase in obj.purchases.all()])

    # purchases_display.short_description = '購買記錄'  # 自定義欄位的名稱