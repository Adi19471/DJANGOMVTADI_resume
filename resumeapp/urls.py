from os import stat
from django.urls import path
from resumeapp import views

from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('<int:pk>',views.CandidateView.as_view(),name='candidate')

#  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
]

if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
