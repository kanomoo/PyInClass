print(">> Program Find Maximum Digit <<")
num = None
while num != 0:
    num = int(input("Enter integer number(0-exit) : "))
    if num != 0: print(f"Maximum Digit of interger number {num} = {max(str(num))}")
    else: print("Exit Program")