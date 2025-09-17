# 8_1
# def input_sale():
#     sales = ()
#     for i in range(7):
#         sale = int(input(f"Enter sale day {i+1} : "))
#         sales += (sale,)
#     return sales

# def total_sale(sales : tuple):
#     return sum(sales)

# def com(total):
#     # rate = {20000:10,10000:7.5,5000:5,1000:2.5,1:0}
#     r_com = (20000,10000,5000,1000,1)
#     rate = (10,7.5,5,2.5,1)
#     for i in range(len(rate)):
#         if total > r_com[i]: return rate[i]
#     return None

# def report():
#     result = ""
#     total = total_sale(input_sale())
#     rate = com(total)
#     result += f"\nTotal sale : {total:.2f}\nCommission rate : {rate:.2f}%\nTotal commission : {total * rate / 100:.2f}"
#     print(result)

# report()

# ==============================

# 8_2

# def input_score():
#     scores, score, i = (), None, 0

#     while True:
#         i += 1
#         score = int(input(f"Enter score {i} ( -1 to exit): "))
#         if score != -1: scores += (score,)
#         else: return scores

# def s_grade():
#     scores = input_score()

#     grades = ()
#     score = (80, 70, 60, 50, 0)
#     grade = ("A", "B", "C", "D", "F")
#     for i in scores:
#         for n in range(len(score)):
#             if i > score[n]:
#                 grades += (grade[n],)
#                 break
#     return grades, scores

# def report():
#     grades, scores = s_grade()

#     result = ""
#     head = "| No. | Scores | Grade |"
#     line = "=" * len(head)
#     result += f"{line}\n{head}\n{line}\n"
#     for i in range(len(scores)):
#         result += f"|  {i+1}  |   {scores[i]:3}  |   {grades[i]}   |\n"
#     result += f"{line}\nEnd Program."
#     print(result) 

# report()


# =============================================== List ================================================
#  8_3 

# def input_grade():
#     grades, grade = [], ""
#     while True:
#         grade = input("Enter grade (Q-exit): ").upper()
#         if grade != "Q": grades.append(grade)
#         else: return grades

# def check_point():
#     grade = input_grade()

#     points = []
#     g = ["A","B","C","D","F"]
#     point = [4,3,2,1,0]
#     for i in grade:
#         for n in range(len(g)):
#             if i == g[n]: 
#                 points.append(point[n])
#                 break
#     return points, grade 

# def report():
#     point, grade = check_point()

#     result = ""
#     total = 0
#     head = "|No.|Grade|Point|Total|"
#     line = "=" * len(head)
#     result += f"{line}\n{head}\n{line}\n"
#     for i in range(len(grade)):
#         result += f"| {i+1} |  {grade[i]}  | {point[i]:3.1f} |{(point[i]) * 3:5.2f}|\n"
#         total += (point[i]) * 3
#     result += f"{line}\nGrade Point Average(GPA) : {total / ((i+1) * 3):.2f}"
#     print(result) 

# report()
# ==============================

# 8_4

# def input_sale():
#     sales = []
#     while True:
#         sale = int(input("Enter sale amount(0 - exit) : "))
#         if sale != 0: sales.append(sale)
#         else: return sales

# def report_sale():
#     sale = input_sale()

#     result = ""
#     head = ":Day: Sale Amount :Percent(%):"
#     line = "-" * len(head)
#     result += f"{line}\n{head}\n{line}\n"
#     n = 0
#     for i in sale:
#         n += 1
#         result += f":{n:3}:{i:13.2f}:{"%":^10}:\n"
#     result += f"{line}\nTotal Amount :     {sum(sale):.2f}"
#     print(result) 

# def Main():
#     while True:
#         choice = input("Main Menu\n==========\n1. Input Sale\n2. Report Sale\n3. Exit\nEnter choice :")
#         match choice:
#             case "1": input_sale()
#             case "2": report_sale()
#             case "3": 
#                 print("Exit Program")
#                 break
#             case _: print("No choice, input again.")

# if __name__ == "__main__":
#     Main()

# ==============================

# 8_5

# from random import randint

# def input_num():
#     std = int(input("Enter number of student : "))
#     sub = int(input("Enter number of subject : "))
#     return std,sub

# def rd_score(std = 12,sub = 6):
#     datas = []
#     for i in range(std):
#         data = []
#         for n in range(sub):
#             rd = randint(1,100)
#             data.append(rd)
#         datas.append(data)
#     return datas

# def report():
#     std, sub = input_num()
#     data = rd_score(std,sub)

#     result = ""
#     head = "|No.|"

#     for i in range(len(data[0])):
#         head += f"Sub {i+1}|"
#     line = "-" * len(head)
#     result += f"{line}\n{head}\n{line}\n"

#     for i in range(len(data)):
#         result += f"|{i+1:2} |"
#         for j in range(len(data[0])):
#             result += f" {data[i][j]:3} |"
#         result += "\n"
    
#     result += line
#     print(result) 

# report()

# =============================================== Dictionary ================================================

# 8_6
# from random import randint

# def r_score():
#     scores = {}
#     for i in range(10):
#         rd = randint(0,100)
#         scores[i+1] = rd
#     return scores

# def grade():
#     scores = r_score()

#     grades = {}
#     grade = {80:"A",70:"B",60:"C",50:"D",0:"F"}
    
#     for k, v in scores.items():
#         for i in grade:
#             if v >= i: 
#                 grades[k] = grade[i]
#                 break

#     return grades, scores

# def report():
#     grades, scores = grade()

#     result = ""
#     head = "| No. | Score | Grade |"
#     line = "=" * len(head)
#     result += f"{line}\n{head}\n{line}\n"
#     for i in range(len(grades)):
#         result += f"|  {i+1:2} |  {scores[i+1]:3}  |   {grades[i+1]}   |\n"
#     result += f"{line}"
#     print(result)

# report()

# ==============================

# 8_7
# def input_branch():
#     data = {}
#     for i in range(4):
#         branch = input("Enter branch name : ")
#         sales = []
#         for i in range(4):
#             sale = int(input(f"Enter sales in Quarter {i+1} : "))
#             sales.append(sale)
#         data[branch] = sales
#     return data

# def report():
#     data = input_branch()

#     result = ""
#     head = "| No. | Branch Name | Quarter1 | Quarter2 | Quarter3 | Quarter4 |   Total |"
#     line = "=" * len(head)
#     result += f"{line}\n{head}\n{line}\n"
#     for branch, quater in data.items():
#         result += f"|  1  |{branch:>12} |"
#         for i in range(len(quater)):
#             result += f"{quater[i]:>9.2f} |"
#         result += f"{sum(quater):>8.2f} |\n"
#     result += line
#     return result

# print(report())

# =============================================== Set ================================================

# 8_8
# def report():
#     A = {"IEEE","on",22,"two",40,10,"one"}
#     print(f"Set A have number : {len(A)}\nMember in Set A : ")
#     for i in A:
#         print(i)

# report()

# ==============================

#  8_9

# notuse 
# def add_item(datas = set()):
#     data = input("Enter number : ")
#     datas.add(data)

# def remove_item(datas =set()):
#     re = input("Remove Item\nEnter number to remove : ")
#     datas.remove(re)

# def report():
#     datas = set()
#     while True:
#         choice = input(" 1. Add Item\n 2. Remove Item\n 3. Display Set\n 4. Exit\nEnter choice : ")    
#         match choice:
#             case "1":
#                 datas.add(input("Enter number : "))       
#             case "2":
#                 datas.remove(input("Remove Item\nEnter number to remove : "))
#             case "3":
#                 print(datas)
#             case "4":
#                 print("Exit Program...")
#                 break
    
# report()