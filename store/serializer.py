from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model=Store
        fields = ['name','location','update_time']

    def validate(self, data):
        """
        自定義的驗證方法，確保相同店家名稱不擁有相同的地址
        """
        name = data.get('name')
        location = data.get('location')

        # 檢查是否有相同店家名稱且相同地址的店家存在
        existing_stores = Store.objects.filter(name=name, location=location).exclude(id=self.instance.id if self.instance else None)

        if existing_stores.exists():
            raise serializers.ValidationError("相同店家不能擁有相同的地址")
        return data