print("===========18===========".center(72))####################################################################
from random import randint
l_word = ["ศูนย์" ,"หนึ่ง", "สอง", "สาม", "สี่", "ห้า" ]
r = randint(0,10)
try: word = l_word[r]
except: print("Error เลขลำดับเกินขอบเขตของลิสต์")
else: print(f"{r} อ่านว่า {word}")
finally: print(f"เลขที่สุ่มได้คือ: {r}")
########################################################################
# def remove_list(lst, value):
#     #การลบสมาชิกของลิสต์ หากเราระบุสมาชิกที่ไม่มีอยู่ในลิสต์จะเกิดข้อผิดพลาด
#     #ดังนั้นจึงกำหนดขั้นตอบการลบไว้ในบล็อก try
#     #แต่ไม่ว่าการลบจะสำเร็จหรือไม่ ก็จะคืนค่าลิสต์ผลลัพธ์กลับออกไปเสมอ       *******************
#     try: lst.remove(value)
#     finally: return lst
#
# number_words = ["zero", "one", "two", "three", "four", "five"]
# a = remove_list(number_words,"ten")
# print(*a,sep=", ")
#
# a = remove_list(number_words, "one")
# print(*a,sep=", ")
print("########################################################################")
def remove_list(lst, value):
    try: lst.remove(value)   # แต่ไม่ว่าการลบจะสำเร็จหรือไม่ ก็จะคืนค่าลิสต์ผลลัพธ์กลับออกไปเสมอ
    finally: return lst # finally คือโค้ดที่ จะทำแน่นอน ไม่ว่าจะเกิดข้อผิดพลาดหรือไม่

l_word = ["zero","one","two","three","four","five"]
a = remove_list(l_word,"one")
print(*a,sep=", ")
# *a คือการ "แตกค่าทุกตัวในลิสต์ a อvอกมา" แล้วส่งต่อเข้า print() ทีละตัว โดยไม่ต้องใช้ลูปเอง

a = remove_list(l_word, " ") #.ใส่ try ไว้ไม่ว่ายังไงก็คืนค่า lst
print(*a,sep=", ")
print("===========19===========".center(72))####################################################################
# x = -1
# if x < 0: raise Exception("ข้อมูลเป็นจำนวนลบ") # raise เป็นการสั่งให้แสดงข้อผิดพลาด

# try :
#     x =  1
#     if x < 0: raise Exception("ข้อมูลเป็นจำนวนลบ") #ข้อผิลพลาดตรงนี้
# except Exception as err: print(err)
# else print("ข้อมูลเป็นจำนวนบวก")

try:
    x = -1
    if x < 0: raise Exception("ข้อมูลเป็นจำนวนลบ") #ใช้ try raise จะไม่ทำงานเลยต้องกำหนดใน except
except Exception as err: print(err)
else: print("ข้อมูลเป็นจำนวนบวก")
finally: print("ขอบคุณครับ")
########################################################################
print("===========20===========".center(72))####################################################################
try:
    # a = int(input("ใส่เลขจำนวนเต็มที่มากกว่า 0 >> "))
    a = -1
    assert a > 0, "ต้องกำหนดค่ามากกว่า 0" # assert เป็นการระบุเงื่อนไขที่จะไม่เกิดข้อผิดพลาด
except Exception as err: print(err)
else: print("กำหนดค่าถูกต้อง")
print()
########################################################################
# def func():
#     value = input("กำหนดเลขจำนวนเต็ม 1 - 100 >> ")
#     if not value.isdigit(): #สตริง (string) ที่อยู่ในตัวแปร value มีแต่ ตัวเลขทั้งหมด (0–9) หรือไม่
#         raise Exception("ต้องกำหนดข้อมูลเป็นจำนวนเต็มบวก")
#     assert int(value) <= 100 and int(value) >= 0,"ต้องกำหนดค่าระหว่าง 1 - 100"
#     return value
# try: result = func()
# except Exception as err: print(err)
# else: print("ค่าที่กำหนดคือ:",result)

def func():
    # value = input("กำหนดจำนวนเต็ม 1 - 100 >> ")
    value = "10"
    if not value.isdigit(): raise Exception("ต้องกำหนดตัวเลขเป็นจำนวนเต็ม")
    assert int(value) >= 0 and int(value) <= 100,"ต้องกำหนดจำนวนเต็ม 1 - 100"
    return value
try: value = func()
except Exception as err: print(err)
else: print(f"ค่าของจำนวนคือ : {value}")

# try:
#     num = int(input("กำหนดเลขจำนวนบวก 1-100 >> "))
#     if num < 0: raise Exception("ต้องกำหนดข้อมูลเป็นเลขจำนวนเต็มบวก")
#     assert num <= 100 and num >= 1 , "ต้องกำหนดค่าระหหว่าง 1 - 100"
# except Exception as err:print(err)
# else: print(f"ค่าที่เหลือคือ: {num}")
print("===========21===========".center(72))####################################################################
a = 12
if type(a) is int: print(True)
if type(a).__name__ == "int": print(True) #.__name__ เปรียนเทียบโดยเขียนชนิดข้อมูลในแบบสตริง
if isinstance(a,int): print(True)
print("########################################################################")
a = 123
b = -4.56
c = True
