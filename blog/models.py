from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = tinymce_models.HTMLField()  # wysiwyg
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

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


class Category(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post} - {self.category}"


class Tag(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post} - {self.tag}"


DRAFT = "draft"
PUBLISHED = "published"
STATUSES = (
    (DRAFT, "draft"),
    (PUBLISHED, "published")
)


class PostStatus(models.Model):

    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUSES, default=STATUSES[0])

    def __str__(self):
        return f"{self.status} - {self.post}"

    def get_absolute_url(self):
        return self.post.get_absolute_url()
