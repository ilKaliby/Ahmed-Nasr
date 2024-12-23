from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, amount):
        pass


class NoDiscount(Discount):
    def apply(self, amount):
        return amount


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, amount):
        return amount - (amount * self.percentage / 100)
    
def calculate_price(amount, discount: Discount):
    return discount.apply(amount)


no_discount = NoDiscount()
percentage_discount = PercentageDiscount(10)

print(calculate_price(100, no_discount))   
print(calculate_price(100, percentage_discount)) 
