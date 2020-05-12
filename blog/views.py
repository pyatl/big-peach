from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from blog.models import Category, DRAFT, Post, PostCategory, PostStatus, PostTag, PUBLISHED, Tag
from django.views.generic.list import ListView


class PostListView(ListView):
    ''' Public Posts Page '''
    queryset = PostStatus.objects.filter(status=PUBLISHED)
    template_name = "blog/post_list.html"
