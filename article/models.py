from email.policy import default
from unicodedata import name
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('Ссылка', blank=True, null=True, unique=True, db_index=True)
    text = models.TextField('Текст')
    date = models.DateField('Дата', auto_now_add=True)
    description = models.CharField('Описание', max_length=250)
    article_image = models.ImageField('Изборажение', null=True, upload_to='article/')
    big_status = models.BooleanField('Большая статья', default=False)
    preview_image = models.ImageField('Предварительное изображение', upload_to='article/')
    
    
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})
    

    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['date', 'title']

