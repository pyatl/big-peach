from django.contrib import admin
from .models import ScheduledTweet, Tweet

admin.site.register(ScheduledTweet)
admin.site.register(Tweet)
