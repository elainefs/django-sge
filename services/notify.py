import requests
from django.conf import settings


class Notify:
    def __init__(self):
        self.__base_url = settings.NOTIFICATION_URL

    def send_order_event(self, data):
        requests.post(
            url=f"{self.__base_url}api/v1/webhooks/order/",
            json=data,
            timeout=5,
        )
