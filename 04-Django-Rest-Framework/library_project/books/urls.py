from django.urls import path

from .views import BookListAPIView, book_list_view, BookDetailAPIView, BookDeleteAPIView, BookUpdateAPIView, \
    BookCreateAPIView, BookListCreateAPIView

urlpatterns = [
    path('books/', BookListAPIView.as_view()),
    path('booklistcreate/', BookListCreateAPIView.as_view()),
    path('books/create/', BookCreateAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
    path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    # path('books/', book_list_view)
]