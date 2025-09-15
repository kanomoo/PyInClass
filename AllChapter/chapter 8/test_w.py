def input_sale():
    sales = ()
    for i in range(7):
        sale = int(input(f"Enter sale day {i+1} : "))
        sales += (sale,)
    return sales

def total_sale(sales : tuple):
    return sum(sales)

def com(total):
    # rate = {20000:10,10000:7.5,5000:5,1000:2.5,1:0}
    r_com = (20000,10000,5000,1000,1)
    rate = (10,7.5,5,2.5,1)
    for i in range(len(rate)):
        if total > r_com[i]: return rate[i]
    return None


def report():
    result = ""
    total = total_sale(input_sale())
    rate = com(total)
    result += f"\nTotal sale : {total:.2f}\nCommission rate : {rate:.2f}%\nTotal commission : {total * rate / 100:.2f}"
    print(result)

report()