from django.contrib.sitemaps import Sitemap
from blog.models import PostStatus, PUBLISHED


class BlogSitemap(Sitemap):
    # blog has priority over other pages
    changefreq = 'never'
    priority = 0.7

    def items(self):
        return PostStatus.objects.filter(status=PUBLISHED)

    def location(self, obj):
        return obj.post.get_absolute_url()

    def lastmod(self, obj):
        return obj.post.created
