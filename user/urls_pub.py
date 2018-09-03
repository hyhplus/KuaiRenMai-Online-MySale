from django.conf.urls import url
from mysale import urls
from user import views,views_login,views_pub,views_user

urlpatterns = [
    url(r'^test/$',views_pub.test),

    url(r'index/$',views_pub.index),
    url(r'publish/$',views_pub.publish)
]