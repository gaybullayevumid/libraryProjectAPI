from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)