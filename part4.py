# class bank_account :
#     def __init__(self, name, acc_number, balance):
#         self.name = name
#         self.acc_number = acc_number
#         self.balance = balance
#     def __str__(self):
#         return f"Name: {self.name}, Account No: {self.acc_number}, Balance: {self.balance}"
#     def deposit (self, amount) :
#         self.balance += amount
#         print(f"Deposited amount {amount}. New balance: {self.balance}")
#     def withdraw (self, amount) :
#         if amount <= self.balance :
#             self.balance -= amount 
#             print(f"Withdrawn amount {amount}. New balance: {self.balance}")
#         else :
#             print("Insufficient balance")
# p1 = bank_account("rajesh", 23456789, 10_000)
# print(p1) 
# p1.deposit(2000)
# p1.withdraw(5000)


class book :
    def __init__(self, title, author):
       self.title = title
       self.author = author 
       self.reviews = []
    def add_review (self, rev) :
        self.reviews.append(rev)
    def count_review(self) :
        return len(self.reviews)
    def display_reviews (self):
        if not self.reviews :
            print("no reviews yet!")
        else :
            for i, review in enumerate(self.reviews, start = 1) :
                print(f"{i}. {review}")
b1 = book("ikikgai", "garcia")
b1.add_review("spiritual :)")
b1.add_review("peaceful")
print("total reviews: ", b1.count_review())
b1.display_reviews() 