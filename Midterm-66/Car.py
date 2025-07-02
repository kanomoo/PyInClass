c_p = d_p = p_y = mount = 0
while True:
    head = ">>>   Main Menu   <<<"
    print("=" * len(head))
    print(f" 0. Exit Program\n 1. Input Car Price ({c_p:,.2f})\n 2. Input Down Payment ({d_p:.2f}%)\n"
          f" 3. Input Interest [Per Year] ({p_y:.2f}%)\n 4. Input Month Number({mount})\n 5. Display Installment\n 6. Clear All Data")
    choice = int(input("Select choice : "))
    match choice:
        case 0:
            print("Exit Program...")
            break
        case 1:
            c_p = int(input("Enter car price : "))
        case 2:
            d_p = int(input("Enter down payment(%) : "))
        case 3:
            p_y = float(input("Enter interest( %) per year : "))
        case 4:
            mount = int(input("Enter mount : "))
        case 5:
            print(f"\nPRice car : {c_p:,.2f}")
            print(f"Amount down payment({d_p:.2f}%) : {c_p * (d_p / 100):,.2f}")
            finance = c_p - (c_p * d_p / 100)
            print(f"Amount finance : {finance:,.2f}")
            p_m = p_y / 12 /100
            print(f"Amount interest({p_y:.2f}%) : {finance * p_m * mount:,.2f}")
            interest = finance * p_m * mount
            print(f"Amount net finance : {finance + interest:,.2f}")
            print(f"Amount installment(per month) : {(finance + interest) / mount:,.2f}")
        case 6:
            c_p = d_p = p_y = mount = 0
        case _:
            print("No choice")
    print()