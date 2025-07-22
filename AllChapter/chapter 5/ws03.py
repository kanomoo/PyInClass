num1 = int(input("Etner number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
if num1 > num2:
    if num1 > num3:
        Max = num1
    else:
        Max = num3
else:
    if num2 > num3:
        Max = num2
    else:
        Max = num3
print("Maximum number : ", Max)