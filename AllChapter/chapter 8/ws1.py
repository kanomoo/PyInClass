def check_Point(grade):
    point = 0
    if grade == "A": point = 4
    elif grade == "B": point = 3
    elif grade == "C": point = 2
    elif grade == "D": point = 1
    elif grade == "F": point = 0
    return point

Done = True
while Done:
    grade = input("Enter grade (Q-exit): ").upper()
    grade = grade.upper()
    