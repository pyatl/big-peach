from django.contrib.syndication.views import Feed
from django.urls import reverse

from blog.models import PostStatus, PUBLISHED


class LatestEntriesFeed(Feed):
    title = "PyATL news"
    link = "/"
    description = "Latest blog posts from PyATL.dev"

    def items(self):
        return PostStatus.objects.filter(status=PUBLISHED).order_by('post__created')

    def item_title(self, item):
        return item.post.title

    def item_description(self, item):
        return item.post.body

    def item_link(self, item):
        return reverse(
            'blog_post_detail',
            args=[
                item.post.slug,
                item.post.pk,
            ],
        )
