# name = input("Enter string for Pyramid : ") # RukSomchai
# num = len(name)
# mess = ""
# for i in range(num):
#     mess += (" " * (num - i-1))
#     for n in name[:i+1]:
#         mess += f"{n} "
#     mess += "\n"
# print(mess)

#show in terminal
name = "RukSomchai"
print(f"Enter string for Pyramid : {name}") # RukSomchai
num = len(name)
mess = ""
for i in range(num):
    mess += (" " * (num - i-1))
    for n in name[:i+1]:
        mess += f"{n} "
    mess += "\n"
print(mess)