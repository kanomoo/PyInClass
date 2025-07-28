# name = input("Enter string for Pyramid : ") # RukSomchai
# num = len(name)
# mess = ""
# for i in range(num):
#     mess += (" " * (num - i-1))
#     for n in name[:i+1]:
#         mess += f"{n} "
#     mess += "\n"
# print(mess)

# #show in terminal
# name = "RukSomchai"
# print(f"Enter string for Pyramid : {name}") # RukSomchai
# num = len(name)
# mess = ""
# for i in range(num):
#     mess += (" " * (num - i-1))
#     for n in name[:i+1]:
#         mess += f"{n} "
#     mess += "\n"
# print(mess)

#show in terminal
# num = input("Enter string for pyramid : ")

# num = "RukSomchai"
# num = " ".join(num)
# for i in range(0,len(num),2):
#     print(" " * ((len(num) // 2) - (i // 2)),num[:i+1],sep="")


name,result = input("Enter string for Pyramid : "), ""
for i in name:
    result += i
    result += " "
for i in range(2,len(result)+1,2):
    print(" " * (len(name) - i // 2),result[:i],sep="")