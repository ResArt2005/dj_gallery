from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import handler404, handler500
from . import views
from django.contrib.sitemaps.views import sitemap

app_name = 'main'

handler404 = views.page_404



urlpatterns = [
    path('', views.index, name='index')
]