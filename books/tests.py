from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from .models import Book, Review

TITLE = "Some Title"
AUTHOR = "An Author"
PRICE = 23.00
REVIEWER_NAME = "User"
REVIEWER_EMAIL = "some@email.com"
REVIEWER_PWD = "Password"
REVIEW_TEXT = "blabla"


class BookTests(TestCase):

    def setUp(self):

        self.reviewer = get_user_model().objects.create(
            username=REVIEWER_NAME,
            email=REVIEWER_EMAIL,
            password=REVIEWER_PWD
        )
        self.special_permission = Permission.objects.get(codename='special_status')

        self.book = Book.objects.create(
            title=TITLE,
            author=AUTHOR,
            price=PRICE
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.reviewer,
            review=REVIEW_TEXT
        )

    def test_book_list_view_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)

    def test_book_list_view_authenticated(self):
        self.client.force_login(self.reviewer)
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, TITLE)
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view_with_permissions(self):
        res = self.client.force_login(self.reviewer)
        self.reviewer.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, AUTHOR)
        self.assertContains(response, REVIEW_TEXT)
        self.assertTemplateUsed(response, 'books/book_detail.html')
