from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def article(request, pk):
    # article = Article.objects.get(pk=pk)
    article_pk = get_object_or_404(Article, pk=pk)
    articles_small = Article.objects.exclude(id=pk)
    # article = Article.objects.all()
    
    return render(request, 'article/article.html', {'article': article_pk,
                                                    'article_list': articles_small})
