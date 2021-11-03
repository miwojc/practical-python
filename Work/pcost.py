# pcost.py
import sys

import report

def portfolio_cost(filename):
    ''' 
    Computes the total cost (shares*price) of a portfolio file
    ''' 
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:.2f}')
