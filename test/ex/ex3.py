head = "| Tax Main Menu |"
line, salary = "=" * len(head), 0
while True:
    print(line,head,line,f" 0. Exit\n 1. Input Salary({salary:,.2f})\n 2. Display Tax",sep="\n")
    choice = int(input("Enter choice : "))
    match choice:
        case 0:
            print("\nExit Program ...")
            break
        case 1:
            salary = int(input("Enter salary : "))
        case 2:
            Net_income, total = (salary * 12) - 100000, 0
            print(f"\nSalary :  {salary:,.2f}\nIncome :  {salary * 12:,.2f}\nDiscount : {100000:,.2f}\nNet Income :  {Net_income:,.2f}")
            head2 = f"|         Net     Income      |Tax Rate|{"Tax":^{len("         Net     Income      |Tax Rate")}}:"
            line2 = "=" * len(head2)
            print("\nReport Tax:",line2,head2,line2,sep="\n")
            for i in range(8):
                if i == 0: net, income, tr, tax, price =        1,   150000,  0, "", 0
                elif i == 1: net, income, tr, tax, price =  150001,  300000,  5, "", 0
                elif i == 2: net, income, tr, tax, price =  300001,  500000, 10, "", 0
                elif i == 3: net, income, tr, tax, price =  500001,  750000, 15, "", 0
                elif i == 4: net, income, tr, tax, price =  750001, 1000000, 20, "", 0
                elif i == 5: net, income, tr, tax, price = 1000001, 2000000, 25, "", 0
                elif i == 6: net, income, tr, tax, price = 2000001, 5000000, 30, "", 0
                elif i == 7: net, income, tr, tax, price =        0,5000001, 35, "", 0

                if Net_income > (income - net): t = (income - net+1)
                else: t = Net_income
                Net_income -= (income - net+1)
                price = t * (tr / 100)
                tax = f"{t:,.2f} * {tr/100:.2f}"
                total += price

                if net != 0 :print(f"|{net:>{len("         Net ")},.2f} -{income:>{len(" Income      ")},.2f} |  {tr:>3}%  | {tax:<{len("        Net     In   ")}}|{price:>{len("              ")},.2f} |")
                else: print(f"|{"":>{len("         Net ")}} >{income:>{len(" Income      ")},.2f} |  {tr:>3}%  | {tax:<{len("        Net     In   ")}}|{price:>{len("              ")},.2f} |")
                if Net_income <= 0: break
            print(line2,f"|{"Total Tax":^{len("         1.00 -   150,000.00 |    0%  | 150,000.00 * 0.00    ")}}|{total:>{len("         0.00 ")},.2f} |",line2,sep="\n")
        case _: print("\nNo choice ...")
    print()