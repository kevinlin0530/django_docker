from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# from django.utils import timezone
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
    purchases = models.ManyToManyField('Purchase', related_name='users', blank=True)
    
class Purchase(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add other fields related to the purchase
    # For example, product_name, purchase_date, price, etc.
    product_name = models.CharField(max_length=255)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'birthday', 'phone_number', 'created_at','update_time', 'is_email_verified', 'is_phone_verified']
    search_fields = ('name','gender',)
    ordering = ('name',)
    filter_horizontal = ('purchases',)

    def purchases_display(self, obj):
        return ", ".join([purchase.product_name for purchase in obj.purchases.all()])

    purchases_display.short_description = '購買記錄'  # 自定義欄位的名稱