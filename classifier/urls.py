from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('dictionary/', views.dictionary,name='dictionary')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


