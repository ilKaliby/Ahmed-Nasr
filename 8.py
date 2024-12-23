class Customer:
    def	__init__(self, name, balance=0):  
        self.name = name
        self.balance = balance
        print("The	init	method was called")
        

cust = Customer("Ahmed Nasr") 
print(cust.balance)