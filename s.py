class Order:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] * item['quantity'] for item in self.items)


class OrderPrinter:
    @staticmethod
    def print_order(order):
        for item in order.items:
            print(f"Item: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}")
        print(f"Total: {order.calculate_total()}")

order = Order([{'name': 'Apple', 'price': 1.2, 'quantity': 10},
    {'name': 'Banana', 'price': 0.8, 'quantity': 5}])
OrderPrinter.print_order(order)
