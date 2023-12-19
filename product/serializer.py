from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['store_name','item','price','description','update_time']

    def validate(self, data):
        # 在serializer.is_valid()之後會帶入data內的item，store_name來進行判斷
        item = data.get('item')
        store_name = data.get('store_name')
        existing_item = Product.objects.filter(item=item,store_name=store_name).exclude(id=self.instance.id if self.instance else None)

        if existing_item.exists():
            raise serializers.ValidationError("相同店家不能擁有相同的商品名稱")
        return data