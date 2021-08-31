from django.contrib import admin

from .models import Book


@admin.register(Book)
class PostsModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'rating', 'author', 'publisher', 'pubdate']
    search_fields = ['name', 'author', ]
    ordering = ['name', 'author']
