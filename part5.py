# with open("names.txt", "w") as f:
#     for i in range(5):
#         name = input("enter name: ")
#         f.write(name + "\n")
# with open("names.txt", "r") as f:
#     content = f.read()
#     print(content) 


# with open("log.txt", "a") as f:
#     f.write("program chal gya!")
# with open("log.txt", "r") as f:
#      print(f.read())
    

# numbers = [5, 10, 15, 20, 25]
# new_list = [ num for num in numbers if num > 15 ]
# print(new_list)


# import json
# data = {
#     "mumbai" : 100000 ,
#     "delhi" : 200000 ,
#     "lucknow" : 300000
# }
# with open("cities.json", "w") as f:
#     json.dump(data, f)
# with open("cities.json", "r") as f:
#     data = json.load(f)
# for city, population in data.items():
#     print(f"{city}:{population}")    
# new_city = input("enter city:")
# new_pop = input("enter population:")
# data[new_city] = new_pop
# with open("cities.json", "w") as f:
#     json.dump(data, f)


