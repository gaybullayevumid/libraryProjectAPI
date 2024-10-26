from django.urls import path

from .views import BookListAPIView, book_list_view, BookDetailAPIView

urlpatterns = [
    path('', BookListAPIView.as_view()),
    path('<int:pk>/', BookDetailAPIView.as_view()),
    path('books/', book_list_view)
]