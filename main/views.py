from django.shortcuts import render
from .models import News, Services
# from django.http import HttpResponse

# Create your views here.
def index(request):
    news = News.objects.all()[:4]
    services = Services.objects.all()
    services_first = services[:8]
    services_second = services[8:]
    context = {
        'news': news,
        'services': services_first,
        'services_second': services_second
    }
    
    return render(request, 'main/index.html', context=context)