from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import (
    Post,
    PostCategory,
    PostStatus,
    PostTag,
    PUBLISHED,
)


class PostListView(ListView):
    ''' Public Posts Page '''
    queryset = PostStatus.objects.filter(status=PUBLISHED)
    template_name = "blog/post_list.html"
    paginate_by = 25


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        context['post_categories'] = PostCategory.objects.filter(post__pk=self.kwargs.get('pk'))
        context['post_tags'] = PostTag.objects.filter(post__pk=self.kwargs.get('pk'))
        return context


class PostsByCategoryListView(ListView):
    template_name = "blog/post_list.html"

    def get_queryset(self):
        queryset = PostCategory.objects.filter(
            post__in=Post.objects.filter(poststatus__status=PUBLISHED),
            category__pk=self.kwargs.get('pk'),
        )
        return queryset


class PostsByTagListView(ListView):
    template_name = "blog/post_list.html"

    def get_queryset(self):
        queryset = PostTag.objects.filter(
            post__in=Post.objects.filter(poststatus__status=PUBLISHED),
            tag__pk=self.kwargs.get('pk'),
        )
        return queryset
