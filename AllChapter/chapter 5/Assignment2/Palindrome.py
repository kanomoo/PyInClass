print(">> Program Palindrome Number <<")
num = input("Enter integer number : ")
for i in range(len(num) // 2):
    result = "Palindrome" if num[i] == num[len(num)-1 - i] else result = "Not Palindrome"
print(result)