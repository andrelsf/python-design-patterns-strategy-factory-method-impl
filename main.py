# main.py
from random import random
from services.handler import Payment


if __name__ == "__main__":
    request_input = {
        "type": "DEBIT",
        "value": random()
    }
    response = Payment(request_input).run()
    print(f"Response: {response}")
