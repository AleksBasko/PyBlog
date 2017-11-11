from django.shortcuts import render
from .models import Article, Comments
from django.http.response import HttpResponse


def show(request):
    names = "My name"
    pages = '<html><body><h1>Hello this is %s !!!</h1></body></html>' %names
    return HttpResponse(pages)

def articleList(request):
    articles = Article.objects.all()
    return render(request, 'articleList.html', {'articleList': articles})


def articleSingle(request, article_id=1):
    article = Article.objects.get(id=article_id)
    comments = Comments.objects.filter(comments_article_id=article_id)
    return render(request, 'article.html', {'article': article, 'comments': comments})
