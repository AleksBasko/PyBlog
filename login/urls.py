from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^auth/login/$', views.authLogin, name='authLogin'),
    # url(r'^/auth/logout/$', views.authLogout, name='authLogout'),
]