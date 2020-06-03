from django import template
from blog.models import PostCategory, PostTag

register = template.Library()

@register.filter
def categories(post):
    return PostCategory.objects.filter(post=post)

@register.filter
def tags(post):
    return PostTag.objects.filter(post=post)