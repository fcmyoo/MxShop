from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Goods` instance, given the validated data.
        """
        return Goods.objects.create(**validated_data)
