from random import randint, uniform

from django.core.management.base import BaseCommand

from faker import Faker

from api.models import Book

fake = Faker()


class Command(BaseCommand):
    help = u'Fills database with some data'  # noqa A003

    # fills db with 10 publishers, 15 stores and 20 authors
    def handle(self, *args, **kwargs):
        # optional
        # Book.objects.all().delete()

        # create 1000 books for each publisher
        counter = 0
        books = []
        for i in range(1000):
            counter += 1
            books.append(Book(name=f'Book "{fake.word().title()}"',
                              pages=randint(100, 1100),
                              price=uniform(300, 900),
                              rating=randint(1, 10),
                              author=fake.name(),
                              pubdate=fake.date(),
                              publisher=f'Publisher "{fake.word().upper()}"'))
        Book.objects.bulk_create(books)

        self.stdout.write('done')
