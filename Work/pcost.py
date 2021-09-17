# pcost.py

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    total = 0
    for line in f:
        _, shares, price = line.split(',')
        total += int(shares) * float(price)

print(f'Total cost {total:.2f}')
