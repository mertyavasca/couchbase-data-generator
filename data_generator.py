import random
import time
from faker import Faker

fake = Faker()

def generate_random_bank_data():
    transaction_types = ["DEPOSIT", "WITHDRAWAL", "TRANSFER", "LOAN_PAYMENT"]
    account_types = ["SAVINGS", "CHECKING", "CREDIT_CARD", "LOAN"]
    currencies = ["USD", "EUR", "GBP", "JPY", "TRY"]

    data = {
        "transaction": {
            "_class": "com.example.bank.Transaction",
            "transactionId": fake.uuid4(),
            "transactionDate": int(time.time() * 1000),
            "customer": {
                "customerId": random.randint(1000, 9999),
                "name": fake.name(),
                "email": fake.email(),
                "phone": fake.phone_number(),
            },
            "account": {
                "accountId": random.randint(100000, 999999),
                "accountType": random.choice(account_types),
                "currency": random.choice(currencies),
                "balance": round(random.uniform(100, 10000), 2)
            },
            "transactionDetails": {
                "transactionType": random.choice(transaction_types),
                "amount": round(random.uniform(10, 1000), 2),
                "currency": random.choice(currencies),
                "status": random.choice(["PENDING", "COMPLETED", "FAILED"]),
            }
        }
    }
    return data
