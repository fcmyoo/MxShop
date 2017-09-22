import re
from datetime import datetime
from datetime import timedelta

from django.contrib.auth import get_user_model
from rest_framework import serializers

from MxShop.settings import REGEX_MOBILE
from .models import VerifyCode
User = get_user_model()


class Smsserializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param attrs: 
        :return: 
        """
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已经存在')

        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError('手机号码非法')

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(addtime__gt=one_mintes_ago,mobile=mobile):
            raise serializers.ValidationError('距离上一次发送未超过1分钟')

        return mobile
