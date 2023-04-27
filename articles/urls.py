from django.urls import path
from articles import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ArticleView.as_view(), name='article_view'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='article_detail_view'),
    path('<int:pk>/comment', views.CommentView.as_view(), name='article_detail_view'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)