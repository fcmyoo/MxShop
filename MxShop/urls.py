"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from MxShop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet
from users.views import SmsCodeViewset,UserViewSet
from user_operation.views import UserFavViewSet

# from django.contrib import admin

route = DefaultRouter()
route.register(r'goods', GoodsListViewSet,base_name='goods')
route.register(r'categorys', CategoryViewSet, base_name="categorys")
route.register(r'codes', SmsCodeViewset, base_name="codes")
route.register(r'users', UserViewSet, base_name="users")
route.register(r'userfavs', UserFavViewSet, base_name="userfavs")

# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })

urlpatterns = [
    url(r'^', include(route.urls)),
    url(r'^admin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'docs/', include_docs_urls(title='慕学生鲜')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # drf自带token认真模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^login/', obtain_jwt_token),
    # 商品列表页

]
