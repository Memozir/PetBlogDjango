from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreate

# Create your views here.

class AccountView(TemplateView):

    def get(self, request):
        form = UserCreationForm()

        context = {
            'form': form
        }

        return render(request, template_name='accounts/registration.html', context=context)
