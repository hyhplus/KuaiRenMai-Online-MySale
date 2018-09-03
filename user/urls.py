from django.conf.urls import url
from mysale import urls
from user import views,views_login,views_pub,views_user

urlpatterns = [
    url(r'^test/$',views.test),

    url(r'register/$', views_login.register),
    url(r'^register_handler/$', views_login.register_handler),

    url(r'login/$', views_login.login),
    url(r'login_handler/$', views_login.login_handler),
]