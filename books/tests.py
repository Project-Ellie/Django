from django.test import TestCase
from django.urls import reverse

from .models import Book

TITLE = "Some Title"
AUTHOR = "An Author"
PRICE = 23.00


class BookTests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title=TITLE,
            author=AUTHOR,
            price=PRICE
        )

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, TITLE)
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, AUTHOR)
        self.assertTemplateUsed(response, 'books/book_detail.html')
