from django.contrib.syndication.views import Feed
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = "PyATL news"
    link = "/"
    description = "Latest blog posts from PyATL.dev"

    def items(self):
        return Post.objects.filter(status=Post.PostStatus.PUBLISHED).order_by('created')

    def item_title(self, item):
        return item.post.title

    def item_description(self, item):
        return item.post.body

    def item_pubdate(self, item):
        return item.post.created
