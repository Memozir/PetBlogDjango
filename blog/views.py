from unicodedata import name
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView

from .models import Article


class ArticlesListView(ListView):
    model = Article
    template_name = 'blog/blog.html'
    
    def get_queryset(self):
        articles = Article.objects.filter(big_status=False)
        big_article = Article.objects.get(big_status=True)
        
        queryset = {
            'article_list': articles,
            'big_article': big_article
        }
        
        return queryset


def blog(request):
    # articles = Article.objects.all()
    articles = Article.objects.filter(big_status=False)
    # big_article = Article.objects.filter(big_status=True)
    big_article = Article.objects.get(big_status=True)
    
    context = {
        'article_list': articles,
        'big_article': big_article
    }
    
    return render(request, 'blog/blog.html', context=context)
