class bank_account :
    def __init__(self, name, acc_number, balance ):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance
    def __str__(self):
        return f"Name: {self.name}, Account No: {self.acc_number}, Balance: {self.balance}"
    def deposit (self, amount) :
        self.amount += amount
        print(f"Deposited amount {amount}. New balance: {self.balance}")
    def withdraw (self, amount) :
        if amount <= self.balance :
            self.balance -= amount 
            print(f"Withdrawn amount {amount}. New balance: {self.balance}")
        else :
            print("Insufficient balance")
p1 = bank_account("rajesh", 23456789, 10_000)
print(p1) 