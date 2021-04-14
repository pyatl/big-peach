
import logging
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Post

logger = logging.getLogger(__name__)


class PostListView(ListView):
    ''' Public Posts Page '''
    queryset = Post.objects.filter(status=Post.PostStatus.PUBLISHED)
    template_name = "blog/post_list.html"
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(
            Post,
            pk=self.kwargs.get('pk'),
            status=Post.PostStatus.PUBLISHED
        )
        return context


class PostsByCategoryListView(ListView):
    template_name = "blog/post_list.html"

    def get_queryset(self):
        queryset = Post.objects.filter(
            status=Post.PostStatus.PUBLISHED,
            category__pk=self.kwargs.get('pk'),
        )
        return queryset
