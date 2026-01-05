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

# print("hello")

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


dict = {
    "name" : ["john", "mary", "chris", "luka"],
    "marks" : ["98", "96", "99", "95"]
}
A = "Add a student"
B = "Update marks"
C = "Search a student"
D = "Display all students marks"
opt = input("Option: ")
new_item = "Add a student: "
updation_item = "Update marks: "
fetch_item = "Search a student: "
if "opt" == A : 
     input(new_item)
elif "opt" == B :
     input(updation_item)
elif "opt" == C :
     input(fetch_item)
else :
     print()
print(dict.update(updation_item))
print(dict.update(new_item))
print(dict.get(fetch_item))