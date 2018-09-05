from django.conf.urls import url
from mysale import urls
from user import views,views_login,views_pub,views_reply

app_name = 'comments'
urlpatterns = [
    url(r'^test/$',views_pub.test),

    url(r'index/$',views_pub.index),
    url(r'publish/$',views_pub.publish),
    url(r'publish_handler/$',views_pub.publish_handler),

    url(r'reply/$', views_reply.reply),
    # url(r'^reply/post/(?P<publish_pk>[0-9]+)/$', views_reply.post_comment),

    url(r'comment/d(publish_pk)+/$', views_reply.post_comment),

]