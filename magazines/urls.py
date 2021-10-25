from django.urls import path, re_path
from .views import main_menu, detail_view, CreateArticleView, create_sub_article_view
from django.contrib.auth.views import LoginView

app_name = 'magazines'

urlpatterns = [
    path('', main_menu),
    path('magazine_detail/<pk>/', detail_view, name="detail"),
    re_path(r'^magazine_create$', CreateArticleView.as_view(success_url="/"), name="create-article"),
    re_path(r'^submagazine_create', create_sub_article_view, name="create-subarticle")
    
]
