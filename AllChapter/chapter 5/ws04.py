g = {80:"A",70:"B",60:"C",50:"D",0:"F"}
num = int(input("Enter score : "))  
if 0 < num <= 100:
    for i in g:
        if num >= i and num <= 100:
            grade = g[i]
            break
    print("Score value ",num,", got grade ",grade,sep="")
else: print("Score not in range.")
