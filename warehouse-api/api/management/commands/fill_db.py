from random import randint, uniform

from django.core.management.base import BaseCommand

from faker import Faker

from api.models import Author, Book, Publisher, AuthorBookManyToMany

fake = Faker()


class Command(BaseCommand):
    help = u'Fills database with some data'  # noqa A003

    # fills db with 10 publishers, 15 stores and 20 authors
    def handle(self, *args, **kwargs):
        # optional
        # Publisher.objects.all().delete()
        # Book.objects.all().delete()

        # create 10 publishers
        publishers = [Publisher(name=f'Publisher "{fake.word().title()}"') for index in range(0, 10)]
        Publisher.objects.bulk_create(publishers)

        # create 50 authors
        authors = [Author(name=fake.name(),
                          age=randint(18, 99)) for i in range(0, 50)]
        Author.objects.bulk_create(authors)

        # create 20 books for each publisher
        counter = 0
        books = []
        for publisher in Publisher.objects.all():
            for i in range(20):
                counter = counter + 1
                books.append(Book(name=f'Book "{fake.word().title()}"',
                                  pages=randint(100, 1100),
                                  price=uniform(300, 900),
                                  rating=randint(1, 10),
                                  pubdate=fake.date(),
                                  publisher=publisher))
        Book.objects.bulk_create(books)

        # add authors for each book
        amount_authors = Author.objects.count()
        amount_books = Book.objects.count()
        instances = []
        for book in Book.objects.all():
            instances.append(AuthorBookManyToMany(author_id=Author.objects.get(id=randint(1, amount_authors)),
                                                  book_id=Book.objects.get(id=randint(1, amount_books))))
        AuthorBookManyToMany.objects.bulk_create(instances)

        self.stdout.write('done')
