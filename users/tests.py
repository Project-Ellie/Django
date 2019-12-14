from django.contrib.auth import get_user_model
from django.test import TestCase

import logging

from django.urls import reverse, resolve

from users.forms import CustomUserCreationForm
from users.views import SignupPageView

logger = logging.getLogger(__name__)


class CustomUserTests(TestCase):

    def test_create_user(self):
        logger.info("Testing user creation...")
        User = get_user_model()
        user = User.objects.create_user(
            username="wolfie",
            email="wolfie@zuehlke.com",
            password='testpass123'
        )
        self.assertEqual(user.username, 'wolfie')
        self.assertEqual(user.email, 'wolfie@zuehlke.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        logger.info("Testing superuser creation...")
        User = get_user_model()
        user = User.objects.create_superuser(
            username="superwolfie",
            email="superwolfie@zuehlke.com",
            password='testpass123'
        )
        self.assertEqual(user.username, 'superwolfie')
        self.assertEqual(user.email, 'superwolfie@zuehlke.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
