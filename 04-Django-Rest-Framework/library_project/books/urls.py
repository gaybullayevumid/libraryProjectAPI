from django.urls import path

from .views import BookListAPIView, book_list_view

urlpatterns = [
    path('', BookListAPIView.as_view()),
    path('books/', book_list_view)
]