from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib import messages
from random_username.generate import generate_username
from members.forms import MemberForm


class MemberCreateView(FormView):
    form_class = MemberForm
    template_name = 'members/member_create_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = generate_username()[0]
        exists = User.objects.filter(username=username)
        if exists:
            username = '{0}{1}'.format(generate_username()[0], randint(1, 999))

        User.objects.create(
            email=form.cleaned_data['email'],
            username=username
            )
        messages.success(self.request, 'Welcome to PyATL!')
        return super().form_valid(form)
