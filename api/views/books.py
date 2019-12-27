from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from books.models import Book
from ..serializers import BookApiSerializer


class BookApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookApiSerializer
