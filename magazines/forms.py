from django.forms import ModelForm
from .models import SubArticle, Article

class CreateArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'description']

class CreateSubArticleForm(ModelForm):
    class Meta:
        model = SubArticle
        fields = ['name', 'description', 'image', 'article']
    

    