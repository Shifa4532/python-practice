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


# class book :
#     def __init__(self, title, author):
#        self.title = title
#        self.author = author 
#        self.reviews = []
#     def add_review (self, rev) :
#         self.reviews.append(rev)
#     def count_review(self) :
#         return len(self.reviews)
#     def display_reviews (self):
#         if not self.reviews :
#             print("no reviews yet!")
#         else :
#             for i, review in enumerate(self.reviews, start = 1) :
#                 print(f"{i}. {review}")
# b1 = book("ikikgai", "garcia")
# b1.add_review("spiritual :)")
# b1.add_review("peaceful")
# print("total reviews: ", b1.count_review())
# b1.display_reviews() 


class student:
    def __init__(self, name, roll_no, marks) : 
       self.__name = name
       self.__roll_no = roll_no
       self.__marks = marks
    def get_name (self) :
        return self.__name 
    def set_name (self, name) :
        if isinstance(name, str) and name.strip() != "" :
          self.__name = name
        else :
            print("Invalid name! Name cannot be empty.")
    def get_roll_no(self) :
       return self.__roll_no
    def set_roll_no (self, roll_no) :
        if isinstance(roll_no, int) and 1 <= roll_no <= 100:
          self.__roll_no = roll_no
        else :
           print("Invalid roll number! Must be between 1 and 100.")
    def get_marks(self) :
       return self.__marks
    def set_marks(self, marks) :
        if isinstance(marks, (int, float)) and marks >= 0 :
           self.__marks = marks
        else :
            print("Invalid Marks! Marks cannot be negative.")

            