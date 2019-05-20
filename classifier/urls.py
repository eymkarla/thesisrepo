from django.urls import path
from . import views
from classifier.views import ClassifyView, ResultView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', ClassifyView.as_view(), name='home'),
    path('dictionary/', views.dictionary,name='dictionary'),
    path('classify/', views.classifier,name='classify'),
    path('home/', views.classifier,name='home'),
    path('classifier_result/<str:text_input>', ResultView.as_view(),name='classifier_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
