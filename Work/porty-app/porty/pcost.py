# pcost.py

from . import report

def portfolio_cost(filename):
    ''' 
    Computes the total cost (shares*price) of a portfolio file
    ''' 
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} portfoliofile')
    cost = portfolio_cost(args[1])
    print(f'Total cost: {cost:.2f}')


if __name__ == '__main__':
    import sys
    main(sys.argv)
