from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import send_mail


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            # очистка корзины
            cart.clear()

            # отправка сообщения об успешном заказе
            send_mail.delay(order.id)

            return render(request, 'orders/order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order_create.html',
                  {'cart': cart, 'form': form})
