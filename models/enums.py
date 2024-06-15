# models/enums.py
from enum import Enum
from services.payments import DebitPayment, CreditPayment


class PaymentType(Enum):
    DEBIT = "debit_payment"
    CREDIT = "credit_payment"

    def factory(self):
        return getattr(self, self.value)()

    def debit_payment(self):
        return DebitPayment()

    def credit_payment(self):
        return CreditPayment()
