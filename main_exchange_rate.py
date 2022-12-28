from playwright.sync_api import sync_playwright, TimeoutError as e
from prabhuTools import PrabhuForex


def exchange_rate():
    with sync_playwright() as p:
        rate = PrabhuForex(p)
        return rate

us_dollar = exchange_rate().singaporeDollar()

print(f"The latest exchange rate | Rs.{us_dollar}.")