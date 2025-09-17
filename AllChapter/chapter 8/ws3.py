# def getPoint(grade):
#     grades = ["A","B+","B","C+","C","D+","D","F"]
#     values = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
#     for n in range(len(grades)):
#         if grade == grades[n]:
#             return(values[n])

# grades = []
# while True:
#     grade = input("Enter grade (Q-ext): ").upper()
#     if grade == "Q":
#         break
#     else:
#         grades.append(grade)
# result = ("=" * 23)+"\n|No.|Grade|Point|Total|\n"+("="*23)+"\n"
# totalPoint = 0.0
# for n in range(len(grades)):
#     point = getPoint(grades[n])
#     total = point * 3
#     totalPoint += total
#     result += f"|{n+1:2} |{grades[n].center(5)}| {point:3.1f} |{total:5.2f}|\n"
# result += ("="*23)+"\n"
# gpa = totalPoint/(len(grades)*3)
# result += f"Grade Point Average(GPA) : {gpa:5.2f}\n"
# print(result)
# print("End Program.")







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