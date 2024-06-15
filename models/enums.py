# models/enums.py
from enum import Enum
from services.payments import DebitPayment, CreditPayment


class PaymentType(Enum):
    DEBIT = "debit_payment_builder"
    CREDIT = "credit_payment_builder"

    def build(self):
        return getattr(self, self.value)()

    def debit_payment_builder(self):
        return DebitPayment()

    def credit_payment_builder(self):
        return CreditPayment()
