# report.py
import fileparse
from stock import Stock
import tableformat

def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares and price.
    """
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float])
    portfolio = [Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio


def read_prices(filename):
    """
    Read a CSV file of price data into a dict mapping names to prices.
    """
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False))


def make_report(portfolio, prices):
    """
    Create a list of (name, shares, price, change tuples given a portfolio list
    and prices dictionary.
    """
    rows = [] 
    for stock in portfolio:
        current_price = prices[stock.name]
        change = current_price - stock.price
        summary = (stock.name, stock.shares, current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata, formatter):
    """
    Prints a formatted table from a list of (name, shares, price, chagne) tuples.
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    """
    Make a stock report given portfolio and price data files
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Generate the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} portfoliofile pricefile')
    portfolio_report(args[1], args[2], args[3])


if __name__ == '__main__':
    import sys
    main(sys.argv)
