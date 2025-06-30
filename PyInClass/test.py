# while True:
#     m = 0
#     num = input("Enter integer number (0-exit) : ")
#     if int(num) > 0:
#         for i in num:
#             if int(num) >= int(m):
#                 m = i
#     elif int(num) == 0:
#         print("Exit Program")
#         exit()
#     print(f"Maximum Digit of integer number {num} = {m}")

while True:
    num = input("Enter integer number (0-exit) : ")
    if int(num) == 0:
        print("Exit Program")
        exit()
    m = max(str(num))
    print(f"Maximum Digit of integer number {m}")