from django.shortcuts import render, redirect
from .models import Article, Comments
from django.http.response import HttpResponse, Http404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

def articleList(request):
    articles = Article.objects.all()
    return render(request, 'article/articleList.html', {'articleList': articles, 'username': auth.get_user(request).username})


def articleSingle(request, article_id=1):
    article = Article.objects.get(id=article_id)
    comments = Comments.objects.filter(comments_article_id=article_id)
    return render(request, 'article/article.html', {'article': article, 'comments': comments, 'username': auth.get_user(request).username})

def addComment(request):
    if request.method == 'POST':
        # if ("stopAddComment" in request.session):
        #     tile = time.ctime()
        #     return JsonResponse({'errorSession': tile})
        # else:
        article_id = request.POST['id']
        comment_content = request.POST['content']
        forArticle = Article.objects.get(id=article_id)
        newComment = Comments(
            comments_article=forArticle,
            comments_text=comment_content,
        )
        newComment.save()
        # request.session.set_expiry(30)
        request.session['stopAddComment'] = True
        # return render_to_string(request, 'comment.html', {'variable': comment_content})
        return JsonResponse({'html': render_to_string('../templates/ajax-template/comment.html', {'variable': comment_content})})
            # return JsonResponse({'html': render(request, 'comment.html', {'variable': comment_content})})


def writeArticlePage(request):
    return render(request, 'article/writeArticle.html')

def createNewArticle(request):
    if request.method == 'POST':
        theme = request.POST['articleTheme']
        content = request.POST['articleContent']
        newArticle = Article(
            article_title=theme,
            article_text=content,
            article_user=request.user
        )
        newArticle.save()
        return redirect('/')


# def articleLike(request):
#     if request.method == 'POST':
#         article_id = request.POST['id']
#         article = newsListModal.objects.get(id=article_id)
#         article.like += 1
#         article.save()
#         return JsonResponse({'variable': article.like})


# def addLike(request, article_id):
#     try:
#         article = Article.objects.get(id=article_id)
#         article.article_likes += 1
#         article.save()
#     except ObjectDoesNotExist:
#         raise Http404
#     return redirect('/articles/')


