from celery import shared_task

from django.core.mail import send_mail as django_send_mail

from orders.models import Order

import json
import requests
from django.views.decorators.csrf import csrf_exempt


@shared_task
def send_mail(id):
    order = Order.objects.get(id=id)
    message = f'Dear {order.first_name}, in this message we will give you some info about your order'

    django_send_mail('Info about your order', message, 'test@testmail.com', [order.email])


@csrf_exempt
def sent_to_api(name):
    data = {"name": name}
    data_json = json.dumps(data)
    print(data_json)
    requests.post('http://127.0.0.1:8000/api/books/',
        json={"name": name})