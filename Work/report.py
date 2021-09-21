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


def make_report(portfolio, prices):
    """
    Create list of (name, shares, price, change tuples given a portfolio list
    and prices dictionary.
    """
    report = [] 
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        report_line = (stock['name'], stock['shares'], current_price, change)
        report.append(report_line)

    return report


if len(sys.argv) == 3:
    filename_portfolio = sys.argv[1]
    filename_prices = sys.argv[2]
else:
    filename_portfolio = 'Data/portfolio.csv'
    filename_prices = 'Data/prices.csv'

portfolio = read_portfolio(filename_portfolio)
prices = read_prices(filename_prices)

# Generate the report data
report = make_report(portfolio, prices)

# Output the report
headers = ('Name', 'Shares', 'Price', 'Change')
name, shares, price, change = headers
print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10s}')
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
    print(f"{name:>10s} {shares:>10d} {'$'+str(price):>10s} {change:>10.2f}")
