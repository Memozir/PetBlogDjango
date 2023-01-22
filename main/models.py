# from turtle import title
from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Текст новости', max_length=200)
    image = models.ImageField('Изображение новости', upload_to='news/')


    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        

class Services(models.Model):
    title = models.CharField(verbose_name='Название', max_length=127, blank=True)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    more_info = models.TextField(verbose_name='Подробнее', max_length=600, blank=True)
    more_info = models.TextField(verbose_name='Подробнее', max_length=650, blank=True)
    money_limit = models.CharField(verbose_name='Лимит по займу', max_length=127)
    age_start = models.CharField(verbose_name='Начальный возраст', default=18, max_length=127)
    age_end = models.CharField(verbose_name='Конечный возраст', default=65, max_length=127)
    stake = models.FloatField(verbose_name='Процентная ставка', blank=True, null=True)
    text_left_from_stake = models.CharField(verbose_name='Текст слева от процентной ставки', blank=True,
                                            max_length=100)
    text_right_from_stake = models.CharField(verbose_name='Текст слева от процентной ставки', blank=True,
                                            max_length=100)
    url = models.URLField(verbose_name='Ссылка', max_length=250, null=True)
    display = models.BooleanField(verbose_name='Отображение на странице', default=True)
    filter_status = models.BooleanField(verbose_name='Отображение после формы', default=False)
    
    
    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural ='Сервисы'
        ordering = ['id', 'display', 'title']
    