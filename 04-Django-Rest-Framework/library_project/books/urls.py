from django.urls import path

from .views import BookListAPIView

urlpatterns = [
    path('', BookListAPIView.as_view()),
]