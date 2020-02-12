from django.urls import path, include

from . import views

urlpatterns = [
    path('events/', include('events.urls')),
    path('', views.index),
]