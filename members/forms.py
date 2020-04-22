from random import randint
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class MemberForm(ModelForm):
    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user:
            raise forms.ValidationError('User with email address already exists.')
        return email
