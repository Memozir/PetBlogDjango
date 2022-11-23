from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def article(request, slug):
    # article = Article.objects.get(pk=pk)
    article_slug = get_object_or_404(Article, slug=slug)
    articles_small = Article.objects.exclude(slug=slug)
    # article = Article.objects.all()
    
    return render(request, 'article/article.html', {'article': article_slug,
                                                    'article_list': articles_small})
