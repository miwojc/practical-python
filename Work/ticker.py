# ticker.py

import report
import tableformat
from follow import follow
import csv

def filter_symbols(rows, names):
    return (row for row in rows if row['name'] in names)

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]
        
def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows
    
def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row([row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])
    
if __name__ == '__main__':
    lines = follow('Data/stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)