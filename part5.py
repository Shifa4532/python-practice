with open("names.txt", "w") as f:
    for i in range(5):
        name = input("enter name: ")
        f.write(name + "\n")
with open("names.txt", "r") as f:
    content = f.read()
    print(content) 


