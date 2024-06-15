# flake8: noqa E501
from abc import ABC, abstractmethod


class Payment(ABC):
    """An interface for each mood of payment."""

    @abstractmethod
    def execute(self, payment: dict) -> bool:
        """Each class will provide its own implementation using this function."""
        pass


class DebitPayment(Payment):

    def __init__(self) -> None:
        print("Initialized 'DebitPayment' class")

    def execute(self, payment: dict) -> bool:
        print(f"{payment.get("type")} payment processed. Price: {payment.get("value")}")
        return True


class CreditPayment(Payment):

    def __init__(self) -> None:
        print("Initialized 'CreditPayment' class")

    def execute(self, payment: dict) -> bool:
        print(f"{payment.get("type")} payment processed. Price: {payment.get("value")}")
        return True