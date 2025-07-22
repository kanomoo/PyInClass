print(">> Program Find Maximum Value <<")
num = int(input("Enter number of value(>= 1) : "))
result,m = "",0 
if num >= 1:
    print(f"\nProgram get value {num} numbers.")
    for i in range(num):
        value = int(input(f"Enter value Number #{i+1} : "))    
        result += f" {value}"
        if i < num-1: result += ","
        if value > m: m = value
    print(f"Your enter number : {result}")
    print(f"Maximum value number is {m}")
else: print("Value input not correct.")
print("Exit Program")

