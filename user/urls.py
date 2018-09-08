from django.conf.urls import url
from mysale import urls
from user import views,views_login,views_pub,views_user,views_index1,views_index

urlpatterns = [
    url(r'^test/$',views.test),

    url(r'register/$', views_login.register),
    url(r'^register_handler/$', views_login.register_handler),

    url(r'login/$', views_login.login),
    url(r'login_handler/$', views_login.login_handler),

    url(r'index/$', views_index),
    url(r'^index_handler/$', views_index1),

    url(r'index1/$', views_index),
    url(r'^index1_handler/$', views_index1),
]