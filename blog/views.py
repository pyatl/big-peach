from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from blog.models import Category, DRAFT, Post, PostCategory, PostStatus, PostTag, PUBLISHED, Tag
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    ''' Public Posts Page '''
    queryset = PostStatus.objects.filter(status=PUBLISHED)
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        context['post_categories'] = PostCategory.objects.filter(post__pk=self.kwargs.get('pk'))
        context['post_tags'] = PostTag.objects.filter(post__pk=self.kwargs.get('pk'))
        return context
