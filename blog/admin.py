from django.contrib import admin
from blog.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        # intercept form to set featured post on save
        if form.data.get('featured'):
            obj.feature()
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
