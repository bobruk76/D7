from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'p_library'
urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorEdit.as_view(), name='author_edit'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),

    path('readers', ReaderList.as_view(), name='reader_list'),
]