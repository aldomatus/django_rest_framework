# rest_framework
from rest_framework import generics
#   Model
from books.models import Book
#   Serializer
from .serializers import BookSerializer

class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer