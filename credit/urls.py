from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('blog.urls')),
    path('', include('article.urls')),
    path('', include('accounts.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
]   
