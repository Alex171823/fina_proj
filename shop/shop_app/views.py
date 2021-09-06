from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from django.views.generic.edit import FormView
from .forms import BookForm


def startpage(request):
    return HttpResponse("You are on the startpage")


class BookListView(ListView):
    model = Book
    template_name = 'books_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BuyView(FormView):
    form_class = BookForm
    template_name = 'buy_book.html'

    def form_valid(self, form):
        # sends email and post to warehouse
        return super().form_valid(form)
