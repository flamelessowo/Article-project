from django.shortcuts import render
from django.views import generic
from .models import Article, SubArticle
from django.shortcuts import render, redirect, reverse
from .forms import CreateArticleForm, CreateSubArticleForm
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.forms import UserCreationForm
def main_menu(request):
    context = {
        'articles': Article.objects.all(),
        'subarticles': SubArticle.objects.all(),
    }
    return render(request, 'main.html', context)

class SignUpView(generic.CreateView):
    template_name="registration/signup.html"
    form_class=UserCreationForm
    
def detail_view(request, pk):
    subarticle = SubArticle.objects.get(id=pk)
    context = {
        "subarticle": subarticle
    }
    return render(request, 'detail_article.html', context)


class CreateArticleView(generic.CreateView):
    template_name = "create_article.html"
    form_class = CreateArticleForm
    
def create_sub_article_view(request):
    form = CreateSubArticleForm()
    if request.method == "POST":
        form = CreateSubArticleForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/')
            
   
    context = {
        'form': form
    }

    return render(request, "create_subarticle.html", context)