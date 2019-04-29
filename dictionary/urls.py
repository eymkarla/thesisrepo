from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dictionary/', views.dictionary,name='dictionary'),
	path('import/', views.impcsv,name='impcsv'),
	path('samples/', views.samples,name='samples'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

