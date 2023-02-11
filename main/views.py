from django.shortcuts import render, redirect
from .models import News, Services
from django.http import HttpResponse

from .forms import ServiceFindFrom


def index(request):
    news = News.objects.all()[:4]
    services = Services.objects.all()
    services_first = services[:8]
    services_second = services[8:]
    
    form = ServiceFindFrom()
    
    context = {
        'news': news,
        'services': services_first,
        'services_second': services_second,
        'form': form
    }
    
    return render(request, 'main/index.html', context=context)


def service_find(request):
    
    if request.method == 'POST':
        sum = request.POST.get('sum')
        
        return HttpResponse(sum)
