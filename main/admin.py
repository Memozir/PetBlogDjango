from django.contrib import admin
from .models import News, Services


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display', 'filter_status')
    # list_display_links = ('id', 'display')
    search_fields = ('title',)
    list_editable = ('display', 'filter_status') 
    

# Register your models here.
admin.site.register(News)
admin.site.register(Services, ServicesAdmin)
