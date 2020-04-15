from random import randint
from django.forms import ModelForm
from django.contrib.auth.models import User

class MemberForm(ModelForm):
    class Meta:
        model = User
        fields = ('email',)
