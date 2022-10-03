from .models import Book
from .serializer import BookSerializer
from rest_framework import viewsets



class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("review")
    serializer_class = BookSerializer



