from django.db import models
from django.contrib.auth.models import User


class Tweet(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class ScheduledTweet(models.Model):
    scheduled_for = models.DateTimeField()
    published = models.BooleanField()
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    scheduled_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'Scheduled for: {self.scheduled_for.strftime("%B %d %Y - %I:%M %p")}'
