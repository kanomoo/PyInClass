# sales = []
# menuStr = "Main Menu\n=========\n1. Input Sale\n2. Report Sale\n3. Exit\nEnter choice : "
# while True:
#     choice = input(menuStr)
#     if choice == "1":
#         while True:
#             sale = float(input("Enter sale amount(0 - exit) : "))
#             if sale == 0.0: break
#             elif sale > 0.0 : sales.append(sale)
#     elif choice == "2":
#         result = ("-" * 30) + "\nDay: Sale Amount :Percent(%):\n"+("-"*30)+"\n"
#         for n in range(len(sales)):
#             result += f":{(n+1):3}:{sales[n]:12.2f}:{"%".center(10)}:\n"
#         result += ("-" * 30) + "\nTotal Amount : %12.2f" % (sum(sales))
#         print(result)
#     elif choice == "3":
#         break
#     else: print("No choice, input again.")
# print("Exit Program")




def input_sale():
    sales = []
    while True:
        sale = int(input("Enter sale amount(0 - exit) : "))
        if sale != 0: sales.append(sale)
        else: return sales

def report_sale(sale):
    result = ""
    head = ":Day: Sale Amount :Percent(%):"
    line = "-" * len(head)
    result += f"{line}\n{head}\n{line}\n"
    n = 0
    com = {20000:10,10001:7.5,5000:5,1000:2.5,1:0}
    for i in sale:
        n += 1
        rate = 0
        for c in com:
            print(c)
            if i > c : 
                rate = com[c]
                break
        result += f":{n:3}:{i:13.2f}:{rate:8.1f}% :\n"
    result += f"{line}\nTotal Amount :     {sum(sale):.2f}"
    print(result) 

def Main():
    while True:
        choice = input("Main Menu\n==========\n1. Input Sale\n2. Report Sale\n3. Exit\nEnter choice : ")
        match choice:
            case "1": sale = input_sale()
            case "2": report_sale(sale)
            case "3": 
                print("Exit Program")
                break
            case _: print("No choice, input again.")

if __name__ == "__main__":
    Main()