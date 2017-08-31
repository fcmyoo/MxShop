from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from goods.models import Goods
from .filters import GoodsFilter
from .serializers import GoodsSerializer


class GoodsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsFilter
