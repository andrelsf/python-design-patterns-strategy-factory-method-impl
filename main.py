# main.py
from random import randint
from services.handler import Payment


if __name__ == "__main__":
    request_input = {
        "type": "DEBIT",
        "value": randint(100, 1000)
    }
    Payment(request_input).run()

    print()
    request_input = {
        "type": "CREDIT",
        "value": randint(1000, 3000)
    }
    Payment(request_input).run()
