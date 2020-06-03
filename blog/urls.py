from django.urls import path
from blog.views import (
    PostDetailView,
    PostListView,
    PostsByCategoryListView,
    PostsByTagListView,)

urlpatterns = [
    path('category/<slug:slug>/<int:pk>/', PostsByCategoryListView.as_view(), name='blog_posts_by_category'),
    path('tag/<slug:slug>/<int:pk>/', PostsByTagListView.as_view(), name='blog_posts_by_tag'),
    path('<slug:slug>/<int:pk>/', PostDetailView.as_view(), name='blog_post_detail'),
    path('', PostListView.as_view(), name='blog_post_list'),
]