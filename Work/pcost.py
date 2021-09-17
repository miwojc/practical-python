# pcost.py
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        total = 0
        for row in rows:
            _, shares, price = row
            try:
                total += int(shares) * float(price)
            except ValueError:
                print("Couldn't parse", line)
        return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:.2f}')
