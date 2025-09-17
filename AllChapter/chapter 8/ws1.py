# def check_Point(grade):
#     point = 0
#     if grade == "A": point = 4
#     elif grade == "B": point = 3
#     elif grade == "C": point = 2
#     elif grade == "D": point = 1
#     elif grade == "F": point = 0
#     return point

# Done = True
# while Done:
#     grade = input("Enter grade (Q-exit): ").upper()
#     grade = grade.upper()
#     if grade == "Q": Done = False
#     else:
#         value = check_Point(grade)
#         print(f"Point value of {grade} is {value}")
# print("End Program.")

# def Check_point(grade):
#     grades = ("A","B","C","D","F")
#     values = (4,3,2,1,0)
#     for i in range(len(grades)):
#         if grade == grades[i]: return values[i]

# while True:
#     grade = input("Enter grade (Q-exit): ").upper()
#     point = Check_point(grade)
#     if grade != "Q": print(f"Point value of {grade} is {point}")
#     else: break
# print("End Program.")


# def Check_grade(grade: str):
#     check = {"A":4,"B":3,"C":2,"D":1,"F":0}
#     if grade in check: return check[grade]

# while True:
#     grade = input("Enter grade (Q-exit): ").upper()
#     point = Check_grade(grade)
#     if grade != "Q": print(f"Point value of {grade} is {point}")
#     else: break
# print("End Program.")


def input_sale():
    sales = ()
    for i in range(7):
        sale = int(input(f"Enter sale day {i+1} : "))
        sales += (sale,)
    return sales

def total_sale(sales : tuple):
    return sum(sales)

def com(total):
    r_com = (20000,10000,5000,1000,1)
    rate = (10,7.5,5,2.5,1)
    for i in range(len(rate)):
        if total > r_com[i]: return rate[i]
    return None

def report():
    result = ""
    total = total_sale(input_sale())
    rate = com(total)
    result += f"\nTotal sale : {total:.2f}\nCommission rate : {rate:.2f}%\nTotal commission : {total * rate / 100:.2f}"
    print(result)

report()