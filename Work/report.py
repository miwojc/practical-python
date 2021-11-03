# report.py
import csv

def read_portfolio(filename_portfolio):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares and price.
    """
    portfolio = [] 
    with open(filename_portfolio, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                stock = {
                    'name' : record['name'],
                    'shares' : int(record['shares']),
                    'price' : float(record['price'])
                }
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
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
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

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


def print_report(reportdata):
    """
    Prints a formatted table from a list of (name, shares, price, chagne) tuples.
    """
    headers = ('Name', 'Shares', 'Price', 'Change')
    name, shares, price, change = headers
    print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10s}')
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in reportdata:
        print(f"{name:>10s} {shares:>10d} {'$'+str(price):>10s} {change:>10.2f}")


def portfolio_report(portfoliofile, pricefile):
    """
    Make a stock report given portfolio and price data files
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Generate the report data
    report = make_report(portfolio, prices)

    # Print it out
    print_report(report)


def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} portfoliofile pricefile')
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
