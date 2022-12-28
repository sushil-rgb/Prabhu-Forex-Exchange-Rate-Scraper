<p align='center'>
  <a href = 'https://www.prabhubank.com/forex' target='_blank'><img src='https://www.prabhubank.com/assets/backend/uploads/logo.png'></a>
  </p>

# Prabhu-Forex-Exchange-Rate-Scraper:
This is a simple python script for scraping the latest currency exchange rates from a website.

# Prerequisites:
Python 3
pip install requirements.txt

# Usage:
Below are the few code snippets:
```python
# There are 20 available exchange rates: Below are the first five for references:
us_dollar = exchange.rate().usDollar()
euro = exchange.rate().euro()
pound = exchange.rate().poundSterling()
australian_dollar = exchange.rate().australianDollar()
swiss_frank = exchange.rate().swissFrank()

# Run the script by typing the command below from terminal
python main_exchange_rate.py
```
The script will print the latest currency exchange rates to the console.

# Customzation:
You can choose the available exchange rate available in PrabhuForex class in prabhuTools.py

# Disclaimer:
This script is for educational purposes only and is not intended for commercial use. Please do not misuse this script or the website it scrapes.
''
