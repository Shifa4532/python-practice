# salary=int(input("enter your salary: "))
# if salary < 30000:
#    print("tax levied on you is 5%")
# elif (salary >= 30000 and salary <= 70000):
#    print("tax levied on you is 15%")
# else:
#    print("tax levied on you is 25%")


# a=int(input("enter a number a: "))
# b=int(input("enter another number b: "))
# for n in range(a,b+1,1):
#    if n%2 == 0 :
#      print(n)


# n=int(input("enter a number: "))
# def give_digits(n):
#     if n==0:
#         return
#     give_digits(n // 10)
#     print(n % 10) 
# give_digits(n)


# n=int(input("number: "))
# def get_count(n):
#     if n == 0:
#         return 1 
#     count = 0
#     while n > 0:
#        n //= 10
#        count += 1
#     return count
# print(get_count(n)) 


# n=int(input("enter a no. to get a sum: "))
# def sum_digits(n):
#     if n == 0:
#         return 0
#     return (n % 10) + sum_digits(n // 10) 
# print(sum_digits(n))


# def div_by_3_n_5():
#     for n in range(1,101):
#       if n % 3 == 0 and n % 5 == 0 :
#          print(n)
# div_by_3_n_5()


# while True :
#   n=input("enter any number: ") 
#   if n == "quit" :
#     print("end")
#     break
#   n=int(n)
#   if n > 0 :
#     print("positive")
#   elif n < 0 :
#     print("negative")
#   else:
#     print("zero")


# def calculator (a, b, operation):
#     if operation == "+":
#         return a+b
#     elif operation == "-":
#         return a-b
#     elif operation == "*":
#         return a*b
#     elif operation == "/":
#         return a/b
#     else:
#         print("error")
# result=calculator (5, 4, "+")
# print(result)


# n=int(input("check if num is prime: "))
# def is_prime (n):
#      if n < 2:
#         return False
#      for i in range (2, n):
#          if n % i == 0 :
#             return False
#      return True
# print(is_prime(n))


def guess_num (n):
    if e == n:
        print("yay, you got it!")
    elif e < n :
        print("too low!")
    elif e > n :
        print("too high!")
e=int(input("enter your guess: "))
guess_num(7)