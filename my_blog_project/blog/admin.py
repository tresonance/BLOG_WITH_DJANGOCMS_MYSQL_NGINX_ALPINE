from django.contrib import admin
from .models import Article, ArticleImage, ArticleAuthorImage, Comment, CommentorImage


# Here You must register the table (Class) you declare inside your models.py
admin.site.register(Article)
admin.site.register(ArticleImage)
admin.site.register(ArticleAuthorImage)
admin.site.register(Comment)
admin.site.register(CommentorImage)
