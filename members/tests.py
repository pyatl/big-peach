from django.test import TestCase, Client
from django.contrib.auth.models import User
from members.forms import MemberForm


class MemberModelFormTest(TestCase):

    def setUp(self):
        self.form_data = {'email': 'test@test.com'}
        self.fail_form_data = {'email': 'test@test'}

    def test_member_form_validation_passes(self):
        form = MemberForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_member_form_validation_fails(self):
        form = MemberForm(data=self.fail_form_data)
        self.assertFalse(form.is_valid())

    def test_member_form_save_add_username(self):
        form = MemberForm(data=self.form_data)
        instance = form.save()
        username = instance.username
        instance.refresh_from_db()
        self.assertTrue(instance.username == username)


class MemberCreateViewTest(TestCase):

    def setUp(self):
        self.endpoint = '/members/create/'
        self.email = 'example@test.com'
        self.client = Client()

    def test_member_gets_create_with_uuid(self):
        response = self.client.post(self.endpoint, {'email': self.email})
        user = User.objects.get(email=self.email)
        self.assertTrue(type(user.email) == str)
        self.assertTrue(response.status_code == 302)
        self.assertNumQueries(1)
