from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_link'),
    path('books/', views.BookListView.as_view(), name='books_link'),
    path('book/<int:pk>', views.BookDetailedView.as_view(), name='book_detail_link'),
    path('authors/', views.AuthorListView.as_view(), name = 'authors_link'),
    path('author/<int:pk>', views.AuthorDetailedView.as_view(), name='author_detail_link'),
]