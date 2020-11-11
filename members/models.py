from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Member(models.Model):

    class MemberType(models.TextChoices):
        REGULAR = 'RG', _('Regular')
        RECRUITER = 'RC', _('Recruiter')
        HIRING_MANAGER = 'HM', _('Hiring Manager')

    member_type = models.CharField(
        max_length=2,
        choices=MemberType.choices,
        default=MemberType.REGULAR
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.email

    def is_recruiter(self):
        return self.member_type == self.MemberType.RECRUITER

    def is_hiring_manager(self):
        return self.member_type == self.MemberType.HIRING_MANAGER


class MemberProfile(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.member.user.email
