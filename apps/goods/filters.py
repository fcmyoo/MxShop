import django_filters

from goods.models import Goods


class GoodsFilter(django_filters.FilterSet):
    """
    商品的过滤类
    """
    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte', help_text="最低价格")
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte', help_text="最高价格")

    class Meta:
        model = Goods
        fields = ['price_min', 'price_min']
