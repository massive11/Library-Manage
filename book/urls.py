from django.urls import path
from . import book_info
from django.conf.urls import url
from django.contrib import admin
from book import views

urlpatterns = [
    path('add', book_info.add, name='test'),
    path('info', book_info.bookInfo, name='info'),
    path('delete', book_info.delete, name='delete'),
    path('getCategory', book_info.getCategory, name='getCategory'),
    path('update', book_info.update, name='update'),
    path('bookSearch', book_info.bookSearch, name='bookSearch'),
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
]
