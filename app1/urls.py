from django.urls import path
from . import   views



urlpatterns = [
    path('books/', views.books_api),
    # path('bookcreate/', views.create_book),
    path('books/<int:pk>', views.booksall_api)

    
    ]