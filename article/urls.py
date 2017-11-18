from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.articleList, name='articleList'),
    url(r'^articles/get/(?P<article_id>\d+)$', views.articleSingle, name='articleSingle'),
    url(r'^articles/write/$', views.writeArticlePage, name='writeArticlePage'),
    url(r'^articles/createNewArticle/$', views.createNewArticle, name='createNewArticle'),
    # url(r'^articles/addlike/(?P<article_id>\d+)$', views.addLike, name='addLike'),
    url(r'^articles/comment/', views.addComment, name='addComment'),
]