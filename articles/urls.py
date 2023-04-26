from django.urls import path
from articles import views

urlpatterns = [
    path('articles', views.ArticleView.as_view(), name='article_view'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail_view'),
]