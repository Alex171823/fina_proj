# import requests
# import json
# from shop_app.models import Book
#
#
# def update_db():
#     authors_data = requests.get('http://127.0.0.1:8000/api/authors/').json()
#     publishers_data = requests.get('http://127.0.0.1:8000/api/publishers/').json()
#     books_data = requests.get('http://127.0.0.1:8000/api/books/').json()
#
#     # clears books json from dublicated
#     cleared_books = []
#     for el in books_data:
#         if el not in cleared_books:
#             el['amount'] = 1
#             cleared_books.append(el)
#         if el in cleared_books:
#             cleared_books(el)
#     print(cleared_books)





