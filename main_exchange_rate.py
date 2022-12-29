from playwright.sync_api import sync_playwright, TimeoutError as e
from prabhuTools import PrabhuForex


def exchange_rate():
    with sync_playwright() as p:
        rate = PrabhuForex(p)
        return rate


currency_exchange_rate = exchange_rate().usDollar() * 1.07

print(currency_exchange_rate)