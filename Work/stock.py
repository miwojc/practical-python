# stock.py

from typedproperty import String, Integer, Float

class Stock:
    '''
    An instance of stock holding consisting of name, shares, and price
    '''
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
        
    @property
    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares * self.price

    def sell(self, amount):
        '''
        Sell a number of shares
        '''
        self.shares -= amount

