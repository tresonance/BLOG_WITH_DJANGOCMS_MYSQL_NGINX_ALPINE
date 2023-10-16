#-*- coding: utf-8 -*-


from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from . import views


app_name = 'blog'  # Remplacez 'votre_application' par le nom de votre application

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('articles/<str:chosen_category_name>/', views.articles_with_chosen_category, name='articles_with_chosen_category'),
    path('articles/<int:article_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comments/<int:comment_id>/add_commentor_image/', views.add_commentor_image, name='add_commentor_image'),
    # Ajoutez d'autres URL pour vos vues si nécessaire
]
