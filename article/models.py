from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    class Meta():
        db_table = 'article'
        ordering = ["-article_date"]
    article_title = models.CharField(max_length=200)
    article_text = models.TextField(null=True)
    article_date = models.DateTimeField(auto_now_add=True, null=True)
    article_likes = models.IntegerField(default=0)
    article_user = models.ForeignKey(User, null=True)


class Comments(models.Model):
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)
