#-*- coding: utf-8 -*-


from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    #re_path(r'^$', views.IndexView.as_view(), name='index'),
    #re_path(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #re_path(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    #re_path(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
]