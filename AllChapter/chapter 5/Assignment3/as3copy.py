head, salary, discount, result = "| Tax Main Menu |", 0, 100000, ""
line = "=" * len(head)
while True:
    print(line,head,line,sep="\n")
    print(f" 0. Exit\n 1. Input Salary({salary:,.2f})\n 2. Display Tax")
    choice = int(input("Enter choice : "))
    match choice:
        case 1: salary = int(input("Enter salary : "))
        case 2:
            income  = salary * 12
            net = income - discount
            print(f"Salary :  {salary:,.2f}\nIncome :  {income:,.2f}\nDiscount :  {discount:,.2f}\nNet income :  {net:,.2f}\n\nReport Tax:")
            line2 = "=" * 78
            head2 = f"|         Net     Income      |Tax Rate|{"Tax":^37}|"
            if salary >= 1 and salary <= 150000:
                p, tax1, tax2, tax= f"   {1:10,.2f} -   {150000:10,.2f} ", f"    {0}%  ", f" {"150,000.00 * 0.00":21}", f"{150000 * 0:14,.2f}"
                result += f"|{p}|{tax1}|{tax2}|{tax}|\n"
            if salary >= 150001 and salary <= 300000: 
                p, tax1, tax2, tax= f"   {150001:10,.2f} -   {300000:10,.2f} ", f"    {5}%  ", f" {f"{150000:,.2f} * {0.05:,.2f}"}:21", f"{salary * 0.05:14,.2f}"
                result += f"|{p}|{tax1}|{tax2}|{tax}|\n"
            if salary >= 300001 and salary <= 500000:
                p, tax1, tax2, tax= f"   {300001:10,.2f} -   {500000:10,.2f} ", f"    {5}%  ", f" {"150,000.00 * 0.00":21}", f"{300000 * 0.05:14,.2f}"
                result += f"|{p}|{tax1}|{tax2}|{tax}|\n"
            print(line2,head2,line2,sep="\n")
            print(result)
    print()