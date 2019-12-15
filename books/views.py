from common.views import AuthenticatedListView, AuthorizedDetailView

from .models import Book


class BookListView(AuthenticatedListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'


class BookDetailView(AuthorizedDetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    permission_required = 'books.special_status'
