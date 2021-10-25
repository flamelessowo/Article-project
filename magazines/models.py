from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class SubArticle(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    