from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^show/$', views.show, name='showt'),
    url(r'^articles/$', views.articleList, name='articleList'),
    url(r'^articles/get/(?P<article_id>\d+)$', views.articleSingle, name='articleSingle'),
    url(r'^articles/addlike/(?P<article_id>\d+)$', views.addLike, name='addLike'),
]