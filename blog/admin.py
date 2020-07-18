from django.contrib import admin
from blog.models import Category, Post, PostCategory, PostStatus, PostTag, Tag


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(PostCategory)
admin.site.register(PostTag)
admin.site.register(PostStatus)
