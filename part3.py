# str=input("enter a string: ")
# if str == str[::-1] :
#     print("it's a palindrome!")
# else:
#     print("it's not a palindrome.")


# nums=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# total = 0
# for x in nums:
#     total += x
# avg = total / len(nums)
# print(avg)


# list_1=list(map(int, input("enter a list: ").split()))
# list_2=list(map(int, input("enter another list:").split()))
# for x in list_2:
#     list_1.append(x)
# list_1.sort()
# print(list_1)

# print("hello") by huda

# tup=(1, 2, 3, 4, 5, 6, 7, 8, 9)
# even = []
# odd = []
# for x in tup :
#     if x % 2 == 0 :
#        even.append(x)
#     else:
#         odd.append(x)
# even=tuple(even)
# odd=tuple(odd)
# print(even)
# print(odd)


# students = {}
# while True :
#      print('''A - Add a student
# B - Update marks
# C - Search for a student
# D - Display all students and marks
# E - Exit''')
#      opt = input("Option: ").upper()
#      if opt == "A":
#           name = input("Enter name: ")
#           marks = int(input("Enter marks: "))
#           students[name]= marks
#           print("Student added successfully")
#      elif opt == "B":
#           name = input("Enter name: ")
#           if name in students :
#                marks = int(input("Enter marks: "))
#                students[name]= marks
#                print("Marks updated successfully")
#           else:
#                print("Student not found!") 
#      elif opt == "C":
#           name = input("Enter name: ")
#           if name in students:
#                print("Marks: ", students[name])
#           else:
#                print("Student not found!") 
#      elif opt == "D":
#           if not students :
#               print("No students found!")
#           else :
#                for name, marks in students.items():
#                     print(name, ":", marks)
#      elif opt == "E":
#           print("Exiting program...")  
#           break
#      else:
#           print("Invalid option")  


# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# dict = {}
# for i in words :
#      dict[i] = len(i)
# print(dict)


# sentence = input("enter: ")
# count = 0
# for ch in sentence:
#    if ch == " " :
#       count += 1 
# print(count)


# list1 = list(map(int, input("enter a list of nums: ").split()))
# list2 = list(map(int, input("enter another list of nums: ").split()))
# found = False
# for el in list1 :
#     if el in list2 :
#         found = True
#         break
# if found :
#     print("common!")
# else :
#     print("not common!")


def print_duplicates(lst):
    # Count occurrences of each element
    count_dict = {}
    for element in lst:
        count_dict[element] = count_dict.get(element, 0) + 1
    
    # Print elements that appear more than once
    print("Elements appearing more than once:")
    for element, count in count_dict.items():
        if count > 1:
            print(f"{element} (appears {count} times)")

# Example usage
my_list = [1, 2, 3, 2, 4, 5, 1, 6, 7, 1, 8, 2]
print_duplicates(my_list)

