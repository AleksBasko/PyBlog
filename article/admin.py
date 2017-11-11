from django.contrib import admin

from .models import Article, Comments

class ArticleAdd(admin.StackedInline):
    model = Comments
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleAdd]
    # list_display =
    # list_editable =
    # list_max_show_all =
    list_filter = ['article_date']
admin.site.register(Article, ArticleAdmin)
