from django.urls import path

from . import book_info

urlpatterns = [
    path('add', book_info.add, name='test'),
    path('info', book_info.bookInfo, name='info'),
    path('delete', book_info.delete, name='delete'),
    path('get_category', book_info.getCategory, name='get_category'),
    path('update', book_info.update, name='update'),
    path('bookSearch', book_info.bookSearch, name='bookSearch'),
]
