from django import forms
from django.contrib.auth.forms import AuthenticationForm


class ServiceFindFrom(forms.Form):
    
    age_choices = [
        ('1', '18-24'),
        ('2', '25-35'),
        ('3', '35-55'),
        ('4', '55+')
    ]
    
    duration_choices = [
        ('1', 'от 0 до 10'),
        ('2', 'от 10 до 20'),
        ('3', 'от 20 до 30'),
        ('4', 'от 30 и дольше')
    ]
        
    is_autstanding_choices = [
        ('true', 'Да'),
        ('false', 'Нет')
    ]
    
    how_get_choices = [
        ('hand', 'В руки'),
        ('card', 'На карту')
    ]
    
    age = forms.ChoiceField(choices=age_choices, widget=forms.RadioSelect)
    sum = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Укажите сумму'}),
                                 max_length=10)
    duration = forms.ChoiceField(choices=duration_choices, widget=forms.RadioSelect)
    is_autstanding = forms.ChoiceField(choices=is_autstanding_choices, widget=forms.RadioSelect)
    how_get = forms.ChoiceField(choices=how_get_choices, widget=forms.RadioSelect)
