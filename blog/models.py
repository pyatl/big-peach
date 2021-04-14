from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from tinymce import models as tinymce_models


class Category(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostStatus(models.TextChoices):
        DRAFT = 'D', _('Draft')
        PUBLISHED = 'P', _('Published')

    status = models.CharField(
        max_length=1,
        choices=PostStatus.choices,
        default=PostStatus.DRAFT,
    )
    featured = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = tinymce_models.HTMLField()  # wysiwyg
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse(
            'blog_post_detail',
            args=[
                self.slug,
                self.pk,
            ],
        )

    def feature(self):
        posts = Post.objects.all()
        for post in posts:
            post.featured = False
            post.save()

        self.featured = True
        self.save()

    def author_name(self):
        if self.author.first_name and self.author.last_name:
            return f'{self.author.first_name} {self.author.last_name}'
        elif self.author.first_name:
            return self.author.first_name
        else:
            return self.author


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post} - {self.category}"
