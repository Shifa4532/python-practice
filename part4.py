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


# class student:
#     def __init__(self, name, roll_no, marks) : 
#        self.__name = name
#        self.__roll_no = roll_no
#        self.__marks = marks
#     def get_name (self) :
#         return self.__name 
#     def set_name (self, name) :
#         if isinstance(name, str) and name.strip() != "" :
#           self.__name = name
#         else :
#             print("Invalid name! Name cannot be empty.")
#     def get_roll_no(self) :
#        return self.__roll_no
#     def set_roll_no (self, roll_no) :
#         if isinstance(roll_no, int) and 1 <= roll_no <= 100:
#           self.__roll_no = roll_no
#         else :
#            print("Invalid roll number! Must be between 1 and 100.")
#     def get_marks(self) :
#        return self.__marks
#     def set_marks(self, marks) :
#         if isinstance(marks, (int, float)) and marks >= 0 :
#            self.__marks = marks
#         else :
#             print("Invalid Marks! Marks cannot be negative.")
#     def __str__(self) :
#        return f"Name: {self.__name}, Roll No: {self.__roll_no}, Marks: {self.__marks}"
# s1 = student("rama", 35, 96.7)
# print(s1) 


# class shape :
#     def area (self) :
#        pass 
# class circle (shape):
#     def area (self) :
#        print("pi*r^2")
# class rectangle (shape) :
#     def area (self) :
#         print("l*b")
# class triangle (shape) :
#     def area (self) :
#         print("1/2*b*h")
# s1 = circle()
# s2 = rectangle()
# s1.area()
# s2.area()


# class vehicle :
#     def __init__(self, brand, model) :
#        self.brand = brand
#        self.model = model
# class car (vehicle) :
#     def __init__(self, brand, model, seats) :
#         super().__init__(brand, model)
#         self.seats = seats
# class bike (vehicle) :
#     def __init__(self, brand, model, engine_cc) :
#         super().__init__(brand, model)
#         self.engine_cc = engine_cc 
# c1 = car("toyota", "camry", 5 )
# print(c1.brand, c1.model, c1.seats)
# c2 = bike("yamaha", "r15", 155)
# print(c2.brand, c2.model, c2.engine_cc)


# from abc import ABC, abstractmethod
# class employee(ABC) :
#     @abstractmethod
#     def calculate_salary(self):
#         pass
# class intern (employee):
#     def calculate_salary(self):
#         return 10000
# class full_time_employee (employee):
#     def calculate_salary(self):
#         return 50000
# class contract_employee (employee):
#     def calculate_salary(self):
#         return 30000
# i1 = intern()
# print(i1.calculate_salary())   


# class person :
#     def __init__(self, name, age = None, address = None):
#         self.name = name
#         self.age = age
#         self.address = address
#     def display (self) :
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
#         print(f"Address:{self.address}")
# p1 = person("shifa", 20, "lucknow")
# p2 = person("shifa", 20)
# p3 = person("shifa")
# print(p1.name, p1.age, p1.address)


class player :
     player_count = 0
     def __init__(self, name, level):
         self.name = name
         self.level = level
         player.player_count += 1
p1 = player("alex", 4)
p2 = player("sara", 5)
p3 = player("max", 3)
print(player.player_count)


# class herbivore :
#     def eats_plant(self):
#         print("eats 🌱.")  
# class carnivore :
#     def eats_meat(self):
#         print("eats 🥩.")  
# class omnivore :
#     def eats_both(self):
#         print("eats both 🥩 and 🌱.")
# class bear (herbivore, carnivore, omnivore) :
#     def info(self):
#         print("Bear is an omnivorous animal 🐻")
# b = bear()
# b.info()
# b.eats_plant()
# b.eats_meat()
# b.eats_both()