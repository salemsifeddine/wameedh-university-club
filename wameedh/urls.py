from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpRequest, request
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as view
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
   
    path("", views.main, name="main"),
    path("earth/", views.earth, name="earth")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
