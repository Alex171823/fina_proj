from celery import shared_task

from django.core.mail import send_mail as django_send_mail

from orders.models import Order


@shared_task
def send_mail(id):
    order = Order.objects.get(id=id)
    message = f'Dear {order.first_name}, in this message we will give you some info about your order'

    django_send_mail('Info about your order', message, 'test@testmail.com', [order.email])
