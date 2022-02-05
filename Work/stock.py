class Stock:
    '''
    An instance of stock holding consisting of name, shares, and price
    '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def sell(self, amount):
        '''
        Sell a number of shares
        '''
        self.shares -= amount

    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"