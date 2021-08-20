from rest_framework import serializers

from .models import Author, Book, AuthorBookManyToMany


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age', ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']


class AuthorBookMTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorBookManyToMany
        fields = ['book_id', 'author_id']

# user = serializers.HiddenField(default=serializers.CurrentUserDefault())
