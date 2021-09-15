from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from django.views.generic.edit import FormView
from .forms import BookForm
from cart.forms import CartAddProductForm


def startpage(request):
    return HttpResponse("You are on the startpage")


class BookListView(ListView):
    model = Book
    template_name = 'book/books_list.html'


def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    cart_product_form = CartAddProductForm()

    return render(request, 'book/book_detail.html', {'product': book,
                                                     'cart_product_form': cart_product_form})


class BuyView(FormView):
    form_class = BookForm
    template_name = 'book/buy_book.html'

    def form_valid(self, form):
        # sends email and post to warehouse
        return super().form_valid(form)
