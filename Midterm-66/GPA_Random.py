from random import randint
total_p = 0
total_c = 0
while True:
    print("=" * 26)
    print(format("Main Menu","^26"))
    print("=" * 26)
    print(" 1. Input number of subject (8)")
    print(" 2. Start Random Grade")
    print(" 3. Exit Program")
    print("=" * 26)
    choice = input("Select your Choice : ")
    match choice:
        case "1":
            num = int(input("Enter your number of subject : "))
            print("Press any key to continue . . .\n")
        case "2":
            print("Start Random  Score&Grade . . . .")
            print("=" * 26)
            for i in range(num):
                point = randint(40,90)
                check_grade = {80:"A",70:"B",60:"C",50:"D",0:"F"}
                for c in check_grade:
                    if point >= c:
                        grade = check_grade[c]
                        break
                check_point = {"A":4,"B":3,"C":2,"D":1,"F":0}
                for c in check_point:
                    if grade == c:
                        point = check_point[c] * 3
                total_p += point
                total_c += 3
                print(f"Your #{i} subject is {grade}")
            print(f"\nYour Total GPA is : {total_p / total_c}")
            print("=" * 26)
            print("Press any key to continue . . .\n")
        case "3":
            print("Exit Program . . .")
            break
        case _:
            print("No choice")


# ทำไว้ show ใน terminal
from random import randint
total_p = 0
total_c = 0
choice = 0 #
while True:
    print("=" * 26)
    print(format("Main Menu","^26"))
    print("=" * 26)
    print(" 1. Input number of subject (8)")
    print(" 2. Start Random Grade")
    print(" 3. Exit Program")
    print("=" * 26)
    choice += 1 #
    print(f"Select your Choice : {choice}") #
    match str(choice):
        case "1":
            num = 5
            print(f"Enter your number of subject : {num}")
            print("Press any key to continue . . .\n")
        case "2":
            print("Start Random  Score&Grade . . . .")
            print("=" * 26)
            for i in range(num):
                point = randint(40,90)
                check_grade = {80:"A",70:"B",60:"C",50:"D",0:"F"}
                for c in check_grade:
                    if point >= c:
                        grade = check_grade[c]
                        break
                check_point = {"A":4,"B":3,"C":2,"D":1,"F":0}
                for c in check_point:
                    if grade == c:
                        point = check_point[c] * 3
                total_p += point
                total_c += 3

                print(f"Your #{i} subject is {grade}")
            print(f"\nYour Total GPA is : {total_p / total_c}")
            print("=" * 26)
            print("Press any key to continue . . .\n")
        case "3":
            print("Exit Program . . .")
            break
