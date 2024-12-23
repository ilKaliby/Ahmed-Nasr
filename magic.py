class Customer:
    
    def __init__(self, name, balance=5):  
        self.name = name
        self.balance = balance
        print("The init method was called")
        
    def __str__(self):
        return 'Customer: ' + str(self.name) + ', balance: ' + str(self.balance)
    
    def __repr__(self):
        return f"Customer(name={self.name}, balance={self.balance})"
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance
   
    def __ge__(self, other):
        return self.balance >= other.balance
    
    def __add__(self, other):
        return Customer(self.name + ' & ' + other.name, self.balance + other.balance)
    
    def __sub__(self, other):
        return Customer(self.name + ' & ' + other.name, self.balance - other.balance)

customer1 = Customer("Alice", 10)
customer2 = Customer("Bob", 7)
customer3 = Customer("Charlie", 10)
