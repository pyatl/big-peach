import logging
from django.core.management.base import BaseCommand
from blog.models import PostCategory, Post, Category

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'migrate v1 posts models data to v2'

    def handle(self, *args, **options):
        post_categories = PostCategory.objects.all()
        for post_category in post_categories:
            post = Post.objects.get(pk=post_category.post.id)
            category = Category.objects.get(pk=post_category.category.id)
            post.category = category
            post.save()

        post_categories.delete()
        logger.info('Finished migration')
