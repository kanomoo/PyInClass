num = int(input("enter number :"))
if num <= 0: print("It's underflow. please try again.")
elif num > 12: print("It's overflow. please try again.")
else:
    for i in range(12): print(f"{num} x {i+1} = {num * (i+1)}")
    
