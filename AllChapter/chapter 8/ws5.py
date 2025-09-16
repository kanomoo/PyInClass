# from random import randint

# def genData(std, sub):
#     scores = []
#     for r in range(std):
#         scores.append([])
#         for c in range(sub):
#             scores[r].append( randint(30,100))
#     return scores

# def reportData( scores):
#     col = 6 * len(scores[0]) + 5
#     line = "-" * col
#     result = "|No.|"
#     for n in range(1,len(scores[0])+1): result += f"sub{n:2}|"
#     result = line + "\n" + result + "\n" + line + "\n"
#     n = 1
#     for score in scores:
#         result += f"|{n:2} |"
#         for s in score: result += f" {s:3} |"
#         result += "\n"
#         n += 1
#     result += line + "\n"
#     print(result)

# def Main():
#     student = int(input("Enter number of student : "))
#     subject = int(input("Enter rnumbero f subject : "))
#     # create list varialbe
#     Scores= genData(student,subject)
#     # generate data in list
#     reportData(Scores)

# # main program
# if __name__ == "__main__":
#     Main()








# ===================================

from random import randint

def input_num():
    std = int(input("Enter number of student : "))
    sub = int(input("Enter number of subject : "))
    return std,sub

def rd_score(std = 12,sub = 6):
    datas = []
    for i in range(std):
        data = []
        for n in range(sub):
            rd = randint(1,100)
            data.append(rd)
        datas.append(data)
    return datas

def report():
    std, sub = input_num()
    data = rd_score(std,sub)

    result = ""
    head = "|No.|"

    for i in range(len(data[0])):
        head += f"Sub {i+1}|"
    line = "-" * len(head)
    result += f"{line}\n{head}\n{line}\n"

    for i in range(len(data)):
        result += f"|{i+1:2} |"
        for j in range(len(data[0])):
            result += f" {data[i][j]:3} |"
        result += "\n"
    
    result += line
    print(result) 

def Main():
    report()
    
if __name__ == "__main__":
    Main()