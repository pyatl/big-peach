from django.urls import path

from blog.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
]