# fake.py 
import pandas as pd
import csv
import random
from faker import Faker
from decimal import Decimal

RECORD_COUNT = 1000
fake = Faker()

currencies = ["CAD", "USD", "EUR", "INR", "CNY", "AUD", "BTC", "JPY", "YER", "MAD"]

def random_currency():
    return random.choice(currencies)

def create_csv_file():
    with open('./fake-file.csv', 'w') as csvfile:
        fieldnames = ['source', 'target', 'amount', 'currency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'source': fake.bban(),
                    'target': fake.bban(),
                    'amount': float(Decimal(random.randrange(5000, 120000))/100),
                    'currency': random_currency(),
                }
            )

if __name__ == '__main__':
    create_csv_file()