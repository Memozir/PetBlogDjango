from django.shortcuts import render, redirect
from .models import News, Services
from django.http import HttpResponse
from django.db.models.functions import Cast
from django.db.models import IntegerField
from django.views.generic import View, FormView, ListView
from django.contrib.auth.forms import UserCreationForm

from .forms import ServiceFindFrom


class ServiceFindFormView(FormView):
    def post(self, request):
        form = ServiceFindFrom(request.POST)

        if form.is_valid():
            sum_value = int(form.cleaned_data['sum'])
                
            services = Services.objects.annotate(
                money_limit_int=Cast('money_limit', output_field=IntegerField())
            ).filter(money_limit_int__gte=sum_value)

            print(services)
            form = ServiceFindFrom()
                
            context = {
                'news': None,
                'services': services,
                'serevices_second': None,
                'form': form
            }

            return render(request, template_name='main/index.html', context=context)
    
    def get(self, request):
        return render(request, template_name='main/index.html', context=None)


def index(request):
    news = News.objects.all()[:4]
    services = Services.objects.all()
    services_first = services[:8]
    services_second = services[8:]
    
    form = ServiceFindFrom()
    # form = UserCreationForm()

    context = {
        'news': news,
        'services': services_first,
        'services_second': services_second,
        'form': form,
    }
    
    return render(request, 'main/index.html', context=context)
