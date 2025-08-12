head2 = ">> Program Calculate Grade <<"
line2, result, tc, tp = "=" * len(head2),"", 0 , 0
print(line2,head2,line2,sep="\n")
print("\nInput Data:")
for i in range(6):
    # name = "A"
    # score = 76
    name = input(f"Enter subject name({i+1}) : ")
    score = float(input(f"Enter subject score({i+1}) : "))
    print()
    if score >= 80 and score <= 100: grade,point = "A",4 * 3
    elif score >= 70 and score <= 79: grade,point = "B", 3 * 3
    elif score >= 60 and score <= 69: grade, point = "C", 2 * 3
    elif score >= 50 and score <= 59: grade,point = "D", 1 * 3
    elif score >= 0 and score <= 49: grade, point = "F", 0 * 3
    tc += 3
    tp += point
    result += f":   {i+1}   :{name:<{len(" Subject Name               ")}}: {score:4.1f} :   {grade}   :   {3}   : {point:4.1f} :\n"
head = ":Sub No.: Subject Name               : Mark : Grade :Credits:Points:"
line = "=" * len(head)
result += line
print(format("Grade Report",f">{len(":Sub No.: Subject Name  "+"Grade Report")}"),line,head,line,result,sep="\n")
print(f":{"Total":>{len("Sub No.: Subject Name               :")}}              :  {tc}   : {tp:4.1f} :",line,sep="\n")
print(f": {f"Grade Point Average (GPA) : {tp / tc:4.2f}":<{len("ub No.: Subject Name               : Mark : Grade :Credits:Points")}}:",line,sep="\n")














# salary = 0
# income = 0
# discount = 100000
# net_income = 0
# while True:
#     print("=" * 17)
#     print("| Tax Main Menu |")
#     print("=" * 17)
#     print(" 0. Exit ")
#     print(" 1. Input Salary","({:,.2f})".format(salary),sep="")
#     print(" 2. Display Tax")
#     choice = input("Enter choice : ")
#     if choice == "0":
#         break
#     elif choice == "1":
#         salary = int(input("Enter salary : "))
#     elif choice == "2":
#         income = salary * 12
#         net_income = income - discount
#         print("Salary :","({:,.2f})".format(salary))
#         print("Income :","({:,.2f})".format(income))
#         print("Discount :","({:,.2f})".format(discount))
#         print("Net Income :","({:,.2f})".format(net_income))
#         print()
#         print("Report Tax:")
#         print("=" * 60)
#         print(f"|{"Net  Income":^17}|Tax Rate|{"Tax":^20}|")
#         if salary <= 150000:
#             print(f"|{"1-150,000.00":>17}|{"0%":>5}|{f"{salary}" "* 0.00":<10}|{(salary * 0.00):>10,}|")