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

# # ทำไว้ show ใน terminal
# num = input("Enter : ")
# for i in range(len(num)):
#     print(" " * i,num[::-1][i:],num[1:(len(num)-i)],sep="")

num,re = input("Enter number : "),""
re += str(int(num) % 10 // 1)
re += str(int(num) % 100 // 10)
re += str(int(num) % 1000 // 100)
re += str(int(num) % 10000 // 1000)
re += str(int(num) % 100000 // 10000)
re += str(int(num) % 1000000 // 100000)
print(re)

# for i in range(1,len(num)+1):
#     re += str(int(num) % (10*i) // (1*i))
# print(re)


