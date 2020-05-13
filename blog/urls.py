from django.urls import path

from blog.views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('<slug:slug>/<int:pk>/', PostDetailView.as_view(), name='blog_post_detail'),
]