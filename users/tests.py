from django.contrib.auth import get_user_model
from django.test import TestCase

import logging

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
