import json
import logging

from celery import shared_task

from django.core.mail import send_mail as django_send_mail

from orders.models import Order

import requests
from requests.exceptions import ConnectionError


logger = logging.getLogger(__name__)


@shared_task
def send_mail(order_id):
    order = Order.objects.get(id=order_id)
    message = f'Dear {order.first_name}, in this message we will give you some info about your order'

    django_send_mail('Info about your order', message, 'test@testmail.com', [order.email])


@shared_task
def send_to_api(name):
    try:
        data = {"name": name}
        data_json = json.dumps(data)

        # change for warehouse prod server URL
        requests.post('http://127.0.0.1:8080/api/recieve/', data_json)

    except ConnectionError:
        logger.error(f'Sending order to api failed, name of book: {name}')
