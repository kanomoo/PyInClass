# แบบไม่เปิด def
n = 0
total,hot, ice, frappe = 0, 0, 0, 0
while True:
    print("=" * 25)
    print(f"{"Drink menu":^25}")
    print("=" * 25)
    print(f"| {"0. Quit":<21} |")
    print(f"| {"1. Hot Coffee":<21} |")
    print(f"| {"2. Ice Coffee":<21} |")
    print(f"| {"3. Frappe Coffee":<21} |")
    print(f"| {"4. Calculate Cost":<21} |")
    print("=" * 25)
    select = input("Select Item : ")
    match select:
        case "0":
            break
        case "1":
            hot = int(input("How Coffee, how many glasses : "))
        case "2":
            ice = int(input("Ice Coffee, how many glasses : "))
        case "3":
            frappe = int(input("Frappe Coffee, how many glasses: "))
        case "4":
            n += 1
            print(f"\nOrder #{n}")
            print("-" * 29)
            print("Qty Item       Price   Total")
            print("-" * 29)
            ph = hot * 30
            pi = ice * 50
            pf = frappe * 60
            total = ph + pi + pf
            if hot > 0:
                print(f"{hot} {"Hot Coffee":<14}30.00  {total:.2f}")
            elif ice > 0:
                print(f"{ice} {"ice Coffee":<14}50.00  {total:.2f}")
            elif frappe > 0:
                print(f"{frappe} {"frappe Coffee":<14}60.00  {total:.2f}")
            print("-" * 29)
            print(f"Total: {total:.2f} Bath\n")
            total, hot, ice, frappe = 0, 0, 0, 0
        case _:
            print("No Select")
# รอบ 2



# แบบเปิด def งานนี้ไม่ค่อยจำเป็นที่ต้องเปิด def
# def hot_coffee():
#     hot_data = []
#     glasses = int(input("Hot Coffee, how many glasses : "))
#     price = 35.00
#     total = price * glasses
#     hot_data.append(glasses)
#     hot_data.append("Hot coffee")
#     hot_data.append(price)
#     hot_data.append(total)
#     return hot_data
#
# def ice_coffee():
#     ice_data = []
#     glasses = int(input("ice Coffee, how many glasses : "))
#     price = 40.00
#     total = price * glasses
#     ice_data.append(glasses)
#     ice_data.append("ice coffee")
#     ice_data.append(price)
#     ice_data.append(total)
#     return ice_data
#
# def frappe_coffee():
#     frappe_data = []
#     glasses = int(input("frappe Coffee, how many glasses : "))
#     price = 50.00
#     total = price * glasses
#     frappe_data.append(glasses)
#     frappe_data.append("frappe coffee")
#     frappe_data.append(price)
#     frappe_data.append(total)
#     return frappe_data
#
# def caculate(data,order):
#     print(f"\nOrder #{order:.0f}:")
#     print("-" * 29)
#     print("Qty Item      Price   Total")
#     print("-" * 29)
#     print(f"{data[0]} {data[1]:<12} {data[2]:.2f}  {data[3]:.2f}")
#     print("-" * 29)
#     print(f"Total: {data[3]:.2f} Bath")
#
# def report():
#     order = 0
#     while True:
#         print("=" * 25)
#         print(format("Drinks menu","^25"))
#         print("=" * 25)
#         print(f"| {"0. Quit":<22} |")
#         print(f"| {"1. Hot Coffee":<22} |")
#         print(f"| {"2. Ice Coffee":<22} |")
#         print(f"| {"3. Frappe Coffee":<22} |")
#         print(f"| {"4. Calculate Coffee":<22} |")
#         print("=" * 25)
#         select = input("select Item : ")
#         order += 0.5
#         match select:
#             case "0":
#                 print("Quit")
#                 break
#             case "1":
#                 data = hot_coffee()
#             case "2":
#                 data = ice_coffee()
#             case "3":
#                 data = frappe_coffee()
#             case "4":
#                 caculate(data,order)
#             case _:
#                 print("No select")
#
# if __name__ == "__main__":
#     report()