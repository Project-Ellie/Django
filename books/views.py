from common.views import AuthenticatedListView, AuthorizedDetailView
from django.db.models import Q
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


class SearchResultsListView(BookListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query))
