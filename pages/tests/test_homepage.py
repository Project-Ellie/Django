from django.test import TestCase
from django.urls import reverse, resolve

import logging

from pages.views import HomePageView

logger = logging.getLogger(__name__)


class MyHomePageTests(TestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        logger.info("Testing home page status code")
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        logger.info("Testing home page template")
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains(self):
        logger.info("Testing home page content")
        self.assertContains(self.response, 'Homepage')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)