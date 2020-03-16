from django.urls import path, include

from .views import IndexView

urlpatterns = [
    path('events/', include('events.urls')),
    path('', IndexView.as_view(),
        name='index'),
]