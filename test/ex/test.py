head = "| Main  Menu |"
line = "=" * len(head)
while True:
    print(line,head,line," 1. Triangle 1\n 2. Triangle 2\n 3. Triangle 3\n 4. Triangle 4\n 5. Triangle 5\n 6. Exit",sep="\n")
    choice = int(input("Enter Choice : "))
    match choice:
        case 1:
            # name = input("Enter name : ")
            name,re = "somchai", ""
            for i in range(len(name)-1,-1,-1):
                re += name[i]
            for i in range(len(name)):
                print(" " * i,end="")
                for n in range(i,len(name)):
                    print(name[n],end="")
                for n in range(1,len(name)-i):
                    print(re[n],end="")
                print()
