from http.client import responses

from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from yaml import serialize

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status


# Create your views here.

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListAPIView(APIView):
    def get(self, request):

        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books.",
            "books": serializer_data
        }
        return Response(data)

# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailAPIView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
                "status": "Successfull",
                "book": serializer_data,
            }

            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "status": "Does not exists",
                    "message": "Book is not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

# class BookDeleteAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteAPIView(APIView):

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                "status": True,
                "message": "Successfully deleted"
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                "status": False,
                "Message": "Book is not found"
            }, status=status.HTTP_400_BAD_REQUEST)

# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        global book_saved
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                "status": True,
                "message": f"Book {book_saved} updated successfully",
            }
        )

# class BookCreateAPIView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateAPIView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            books = serializer.save()
            data = {
                "status": "Books are saved to the database",
                "books": data
            }
            return Response(data)
        # else:
        #     return Response(
        #         {
        #             "status": False,
        #             "message": "Serializer is not valid"
        #         },
        #         status=status.HTTP_400_BAD_REQUEST
        #     )

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# function based view in DRF
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)