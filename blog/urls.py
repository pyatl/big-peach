from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog.views import (
    PostDetailView,
    PostListView,
    PostsByCategoryListView,
    PostsByTagListView,)
from blog.feeds import LatestEntriesFeed
from blog.sitemap import BlogSitemap


sitemaps = {'blog': BlogSitemap}


urlpatterns = [
    path('category/<slug:slug>/<int:pk>/', PostsByCategoryListView.as_view(), name='blog_posts_by_category'),
    path('tag/<slug:slug>/<int:pk>/', PostsByTagListView.as_view(), name='blog_posts_by_tag'),
    path('<slug:slug>/<int:pk>/', PostDetailView.as_view(), name='blog_post_detail'),
    path('', PostListView.as_view(), name='blog_post_list'),
    path('feed/latest/', LatestEntriesFeed()),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
