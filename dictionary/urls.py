from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dictionary/', views.dictionary,name='dictionary'),
	path('import/', views.impcsv,name='impcsv'),
	path('search_form/', views.search_form,name='search_form'),
	path('search/', views.search,name='search'),
	path('waray_dictionary/', views.waray_dictionary,name='waray_dictionary'),
	path('cebuano_dictionary/', views.cebuano_dictionary,name='cebuano_dictionary'),
	path('hiligaynon_dictionary/', views.hiligaynon_dictionary,name='hiligaynon_dictionary'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

