from django.urls import path

from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('books/', views.BookListView.as_view(), name='books_list'),
    path('books/detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('books/buy/<int:pk>', views.BuyView.as_view(), name='buy')
    ]
