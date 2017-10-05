from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.permissions import IsOwnerOrReadOnly
from .models import UserFav, UserLeavingMessage,UserAddress
from .serializers import UserFavSerializer, UserFavDetailSerializer, LeavingMessageSerializer,UserAddressSerializer


# Create your views here.


class UserFavViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet,
                     mixins.RetrieveModelMixin):
    """
    list:
        获取用户列表收藏
    retrieve:
        获取某个商品是否收藏
    create:
        收藏商品
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    serializer_class = UserFavSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # 修改查询id
    lookup_field = 'goods_id'

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    def get_serializer_class(self):

        if self.action == 'list':
            return UserFavDetailSerializer
        elif self.action == 'create':
            return UserFavSerializer
        return UserFavSerializer


class LeavingMessageViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    """
    list:
        获取留言列表
    destroy:
        删除留言
    create:
        创建留言
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = LeavingMessageSerializer

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class UserAddressViewSet(viewsets.ModelViewSet):
    """
    收货地址管理
    list:
        获取收货地址列表
    delete:
        删除收货地址
    create:
            创建收货地址
    update:
            修改收货地址
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserAddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)