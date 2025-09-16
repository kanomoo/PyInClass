from random import randint

def randomScores(scores):
    for n in range(1,11):
        scores[n] = randint(30, 100)

def checkGrade(scores, grades):
    GRADES = {80:"A",}