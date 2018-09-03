from django.conf.urls import url
from mysale import urls
from user import views,views_login,views_pub,views_user

urlpatterns = [
    url(r'^test/$',views_user.test),

    url(r'^index/$', views_user.index),  # 个人资料
    url(r'^account/$', views_user.account),  # 账户设置
    url(r'^collection/$', views_user.colletion),  # 我的收藏
    url(r'^contact/$', views_user.contact),  # 增加联系
    url(r'^demand/$', views_user.demand),  # 我的需求
    url(r'^message/$', views_user.message),  # 我的消息
    url(r'^mybdhome/$', views_user.mybdhome),  # 个人设置
    url(r'^wallet/$', views_user.walllet),  # 我的钱袋
    url(r'^out/$', views_user.out),  # 退出登录
    url(r'^release/$', views_user.release),  # 发布合作信息
]