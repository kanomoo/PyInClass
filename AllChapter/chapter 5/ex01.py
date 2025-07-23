print(">> Program Find Maximum Digit <<")
num = None
while num != 0:
    num = int(input("Enter integer number(0-exit) : "))
    print(f"Maximum Digit of interger number {num} = {max(str(num))}") if num != 0 else print("Exit Program")