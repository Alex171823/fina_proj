from rest_framework import serializers

from .models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'age']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']

# user = serializers.HiddenField(default=serializers.CurrentUserDefault())
