import random
import time
from faker import Faker

fake = Faker()

def generate_random_data():
    product_types = ["ELECTRONICS", "FURNITURE", "CLOTHING", "FOOD", "TOYS"]
    payment_methods = ["CREDIT_CARD", "PAYPAL", "CRYPTO", "BANK_TRANSFER", "CASH"]
    order_status = ["PENDING", "SHIPPED", "DELIVERED", "CANCELLED", "RETURNED"]
    delivery_options = ["STANDARD", "EXPRESS", "SAME_DAY"]
    
    data = {
        "order": {
            "_class": "com.example.ecommerce.Order",
            "orderId": fake.uuid4(),
            "orderDate": int(time.time() * 1000),
            "customer": {
                "customerId": random.randint(1000, 9999),
                "name": fake.name(),
                "email": fake.email(),
                "phone": fake.phone_number(),
                "address": {
                    "street": fake.street_address(),
                    "city": fake.city(),
                    "state": fake.state(),
                    "postalCode": fake.postcode(),
                    "country": fake.country()
                }
            },
            "items": [
                {
                    "productId": random.randint(10000, 99999),
                    "productName": fake.word().capitalize(),
                    "productType": random.choice(product_types),
                    "quantity": random.randint(1, 5),
                    "price": {
                        "amount": round(random.uniform(5.99, 999.99), 2),
                        "currency": "USD"
                    }
                }
                for _ in range(random.randint(1, 5))
            ],
            "payment": {
                "paymentMethod": random.choice(payment_methods),
                "paymentStatus": random.choice(order_status),
                "transactionId": fake.uuid4()
            },
            "delivery": {
                "deliveryOption": random.choice(delivery_options),
                "deliveryStatus": random.choice(order_status),
                "deliveryDate": int((time.time() + random.randint(1, 10) * 86400) * 1000),
                "trackingId": fake.uuid4()
            },
            "totalAmount": {
                "amount": round(random.uniform(50, 1500), 2),
                "currency": "USD"
            }
        }
    }
    return data
