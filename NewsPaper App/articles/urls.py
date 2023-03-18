# config/urls.py
from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 
from .views import ArticleListView,ArticleUpdateView,ArticleDeleteView,ArticleDetailView,ArticleCreateView

urlpatterns = [
    path('', ArticleListView.as_view(),name='article_list'), # new
    path('<int:pk>/edit', ArticleUpdateView.as_view(),name='article_edit'), # new
    path('<int:pk>/delete', ArticleDeleteView.as_view(),name='article_delete'), # new
    path('<int:pk>/', ArticleDetailView.as_view(),name='article_detail'), # new
    path('new/', ArticleCreateView.as_view(),name='article_new'), # new
]