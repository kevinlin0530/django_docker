from rest_framework import serializers
from .models import User,Purchase
from store.models import Store
from product.models import Product
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import json
class UserSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(input_formats=['%Y-%m-%d'])
    id_number = serializers.CharField(validators=[
            RegexValidator(
                regex=r'^[A-Z][1-2]\d{8}$',
                message='請輸入有效的身分證號碼',
                code='invalid_id_number')
                ])
    class Meta:
        model=User
        fields = ['name','email','birthday','phone_number','id_number','update_time']
    # validate_後面對應的名稱為id_number讓此function處理id_number的身分證處理
    def validate_id_number(self, value):
        local_table =  {'A': 1, 'B': 10, 'C': 19, 'D': 28, 'E': 37, 'F': 46,
            'G': 55, 'H': 64, 'I': 39, 'J': 73, 'K': 82, 'L': 2, 'M': 11,
            'N': 20, 'O': 48, 'P': 29, 'Q': 38, 'R': 47, 'S': 56, 'T': 65,
            'U': 74, 'V': 83, 'W': 21, 'X': 3, 'Y': 12, 'Z': 30}

        
        number = value.replace(' ', '')

        if len(number) != 10:
            raise serializers.ValidationError("請輸入有效的身分證號碼")

        sex = int(number[1])

        if sex != 1 and sex != 2:
            raise serializers.ValidationError("請輸入有效的身分證號碼")

        check_num = local_table[number[0]]

        for i in range(1, 10):
            check_num += int(number[i]) * (9 - i)
            
        check_num = check_num + int(number[9])

        if check_num % 10 == 0:
            return value
        else:
            raise serializers.ValidationError("請輸入有效的身分證號碼")


class PurchaseSerializer(serializers.ModelSerializer):
    # 由於沒有指定pk，導致django內自動產生pk，輸入資料時不能直接輸入名稱所做的處理
    user = serializers.CharField()
    product = serializers.CharField()
    store_name = serializers.CharField()
    class Meta:
        model = Purchase
        fields = ['user','product','store_name','purchase_date']
    # 跟data不同，data 在serializer呼叫時就會帶入，而validated_data 要serializer.is_vailed()後才會帶入資料
    def create(self, validated_data):
        user = validated_data['user']
        products = validated_data['product'].split(',')
        store_names = validated_data['store_name'].split(',')
        purchase_list = []
        for i in range(len(products)):
            try:
                price = Product.objects.get(store_name=store_names[i], item=products[i]).price
            except Product.DoesNotExist:
                raise serializers.ValidationError(f"{products[i]}或{store_names[i]}不存在")

            # 第一個參數用來接參數，第二個參數為布林值，因為不使用，用_來拋棄
            user_instance, _ = User.objects.get_or_create(name=user)
            product_instance, _ = Product.objects.get_or_create(item=products[i],store_name=store_names[i])
            store_instance, _ = Store.objects.get_or_create(name=store_names[i])
            
            if store_instance and product_instance:
                purchase = Purchase.objects.create(
                    user=user_instance,
                    product=product_instance,
                    store_name=store_instance,
                    price=price
                )
                purchase_list.append(purchase)
            else:
                raise serializers.ValidationError("商品或商家不存在")
        return purchase_list
