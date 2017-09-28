import django_filters
from django.db.models import Q

from goods.models import Goods


# 继承类必须为django_filters.rest_framework.FilterSet,否则没确定按钮
class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(name='shop_price', lookup_expr='gte', help_text="最低价格")
    pricemax = django_filters.NumberFilter(name='shop_price', lookup_expr='lte', help_text="最高价格")

    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemin', 'is_hot']
