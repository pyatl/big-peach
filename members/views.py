import logging
from uuid import uuid4
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.contrib import messages
from members.forms import MemberForm
from members.models import Member

logger = logging.getLogger(__name__)


class MemberCreateView(FormView):
    form_class = MemberForm
    template_name = 'members/member_create_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = User.objects.create(
            email=form.cleaned_data['email'],
            username=uuid4().hex
        )
        Member.objects.create(
            user=user
        )
        messages.success(self.request, 'Welcome to PyATL!')
        return super().form_valid(form)
