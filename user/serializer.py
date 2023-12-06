from rest_framework import serializers
from .models import User
from django.core.validators import RegexValidator

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

        