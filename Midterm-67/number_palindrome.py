# num = input("Enter number : ") #123456
# re = num[::-1]
# mess = ""
# for i in range(len(num)):
#     mess += " " * i + re[i:]
#     mess += num[1:len(num) - i] + "\n"
# print(mess)


# # ทำไว้ show ใน terminal
# num = "123456"
# print(f"Enter number : {num}") #123456
# re = num[::-1]
# mess = ""
# for i in range(len(num)):
#     mess += " " * i + re[i:]
#     mess += num[1:len(num) - i] + "\n"
# print(mess)

# ทำไว้ show ใน terminal
num = input("Enter : ")
for i in range(len(num)):
    print(" " * i,num[::-1][i:],num[1:(len(num)-i)],sep="")
