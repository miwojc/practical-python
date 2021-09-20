# report.py
import csv
import sys

def read_portfolio(filename_porfolio):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares and price.
    """
    portfolio = [] 
    with open(filename_portfolio, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            stock = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2]),
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename_prices):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    prices = {} 
    with open(filename_prices, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])

    return prices

if len(sys.argv) == 3:
    filename_portfolio = sys.argv[1]
    filename_prices = sys.argv[2]
else:
    filename_portfolio = 'Data/portfolio.csv'
    filename_prices = 'Data/prices.csv'

portfolio = read_portfolio(filename_portfolio)
prices = read_prices(filename_prices)

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares'] * s['price']

print(f'Total cost {total_cost:.2f}')

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares'] * prices[s['name']]

print(f'Current value {total_value:.2f}')
print(f'Gain {total_value - total_cost:.2f}')
