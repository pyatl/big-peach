from django.contrib.sitemaps import Sitemap
from blog.models import Post


class BlogSitemap(Sitemap):
    # blog has priority over other pages
    changefreq = 'never'
    priority = 0.7

    def items(self):
        return Post.objects.filter(status=Post.PostStatus.PUBLISHED)

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.created
