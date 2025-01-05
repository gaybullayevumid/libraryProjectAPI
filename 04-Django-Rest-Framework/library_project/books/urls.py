from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    # path('books/', BookListAPIView.as_view()),
    # path('booklistcreate/', BookListCreateAPIView.as_view()),
    # path('bookupdatedelete/<int:pk>/', BookUpdateDeleteView.as_view()),
    # path('books/create/', BookCreateAPIView.as_view()),
    # path('books/<int:pk>/', BookDetailAPIView.as_view()),
    # path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
    # path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    # # path('books/', book_list_view)
]

urlpatterns = router.urls + urlpatterns