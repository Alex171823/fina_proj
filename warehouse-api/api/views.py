from rest_framework import viewsets

from .models import Author, Book, AuthorBookManyToMany
from .serializers import AuthorSerializer, AuthorBookMTMSerializer, BookSerializer


class AuthorModelApi(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookModelApi(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorBookMTMModelView(viewsets.ModelViewSet):
    queryset = AuthorBookManyToMany.objects.all()
    serializer_class = AuthorBookMTMSerializer
