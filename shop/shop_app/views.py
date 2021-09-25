from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
from .models import Book
from django.views.generic.edit import FormView
from .forms import BookForm
from cart.forms import CartAddProductForm
from cart.cart import Cart


def startpage(request):
    return HttpResponse("You are on the startpage")


class BookListView(ListView):
    model = Book
    template_name = 'book/books_list.html'


def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    cart = Cart(request)
    form = CartAddProductForm(product=book, cart=cart)

    if request.method == 'POST':
        form = CartAddProductForm(data=request.POST, product=book, cart=cart)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=book,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
            return redirect('cart_detail')

    return render(request, 'book/book_detail.html', {'product': book,
                                                     'cart_product_form': form})


class BuyView(FormView):
    form_class = BookForm
    template_name = 'book/buy_book.html'

    def form_valid(self, form):
        # sends email and post to warehouse
        return super().form_valid(form)
