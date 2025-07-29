print(">> Program Palindrome Number <<")
num = input("Enter integer number : ")
for i in range(len(num) // 2):
    start = num[i]
    end = num[len(num)-1 - i]
    if start == end: result = "Palindrome"
    else: result = "Not Palindrome"
print(result)