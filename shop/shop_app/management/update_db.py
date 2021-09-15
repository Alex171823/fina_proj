import requests
from shop_app.models import Book


def update():
    print('Starting update from warehouse api for database')
    print('Getting data from api...')

    # get json from wharehouse api
    authors_data = requests.get('http://127.0.0.1:8000/api/authors/').json()
    publishers_data = requests.get('http://127.0.0.1:8000/api/publishers/').json()
    books_data = requests.get('http://127.0.0.1:8000/api/books/').json()

    print('Clearing data...')
    # clears books json from dublicated and count amount of each type of book
    cleared_books = []
    for el in books_data:
        if el in cleared_books:
            cleared_books[cleared_books.index(el)]['amount'] += 1
        elif el not in cleared_books:
            el['amount'] = 1
            cleared_books.append(el)

    print('Adding data to database...')
    data_to_update_db = []
    for book in cleared_books:
        # gets authors names for each book
        authors = ''
        for i in book['authors']:
            authors += authors_data[i - 1]['name']

        data_to_update_db.append(Book(name=book['name'],
                                      pages=book['pages'],
                                      price=book['price'],
                                      rating=book['rating'],
                                      authors=authors,
                                      publisher=publishers_data[book['publisher'] - 1]['name'],
                                      pubdate=book['pubdate'],
                                      amount=book['amount']))

    Book.objects.bulk_update_or_create(data_to_update_db, ['name',
                                                           'pages',
                                                           'price',
                                                           'rating',
                                                           'authors',
                                                           'publisher',
                                                           'pubdate'], match_field='name')

    print('Database was updated from warehouse api')
