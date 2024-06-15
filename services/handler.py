# flake8: noqa E501
# services/handler.py
from models.enums import PaymentType


class Payment:

    def __init__(self, payment_input: dict) -> None:
        self._payment_input = payment_input
        self._payment_type = payment_input['type']

    def run(self):
        response = PaymentType[self._payment_type].build().execute(self._payment_input)
        return response