import random
import string
rd = random.randint
#1
num = rd(0,10)
print(num,"คู่" if num % 2 == 0 else "คี่")
#2
num = rd(1,100)
print(num,"เด็ก" if 0 < num < 18 else "ผู้ใหญ่")
#3
print(num,"ผ่าน" if num >= 50 else "ไม่ผ่าน")
#4
num =rd(-100,100)
print(num,"บวก" if num > 0 else "ลบ")
#5
num = rd(0,1)
print(num,"เท่ากับ 0" if num == 0 else "ไม่เท่ากับ 0")
#6
char = string.ascii_lowercase[rd(0,25)]
print(char,"สระ" if char.upper() in ["A","E","I","O","U"] else "พยัญชนะ")
#7
name = random.choice(["few","","jerm"])
print(name,f"สวัสดีคุณ [{name}]" if name != "" else "")
#8
num1,num2 = rd(0,100),rd(0,100)
print(num1,num2,":",(f"{num1} มากกว่า {num2}" if num1 > num2 else f"{num2} มากกว่า {num1}")
if num1 != num2 else f"{num1} เท่ากับ {num2}")
#9
num = rd(0,100)
print(num,"คุณสามารถขับรถได้" if num >= 18 else "ไม่")
#10
grade = {80:"A",75:"B+",70:"B",65:"C+",60:"C",55:"D+",50:"D",0:"F"}
num = rd(0,100)
for i in grade:
    if num >= i:
        print(num,grade[i])
        break
#11
num = rd(0,30)
print(num,"หาร 3 ลงตัว" if num % 3 ==0 else "หารไม่ลงตัว")
#12
num = rd(0,1000)
print(num,"เป็นเลข 3 หลัก" if 100 < num < 1000 else "ไม่เป็นเลข 3 หลัก")
#13
s = random.choice(["เจิมน่าเจิมมาก","เย้ย"])
print(s,"ความยาวเกิน 10 ตัวอักษร" if len(s) >= 10 else "สั้น")
#14
num1,num2 = rd(0,1),rd(0,1)
print(num1,num2,"เท่ากัน" if num1 == num2 else "ไม่เท่า")
#15
num = rd(0,10)
print(num,"เล็กมาก"if num < 3 else "ไม่เล็ก")
#16
num = rd(0,100)
print(num,"ดีมาก" if num >= 80 else "ไม่ดี")
#17
num = rd(1,12)
month = {1:"jan",2:"feb",3:"mar",4:"apr",5:"may",6:"jun",7:"jul",8:"aug",9:"sep",10:"oct",11:"nov",12:"dec"}
print(num,month[num])
#18
num = rd(-10,10)
print(num,"หนาวมาก" if num < 0 else "ปกติ")
#19
num = rd(0,15)
print(num,"เป็นเลขหลักเดียว"if 0 < num < 10 else "ไม่ใช่")
#20
name = random.choice(["aber","bera"])
print(name,"เริ่มต้นด้วยตัวอักษร A" if str(name[0]).upper() == "A" else "ไม่ใช่")
#21
num = rd(1233,1234)
print(num,"เข้าสู่ระบบสำเร็จ" if num == 1234 else "ไม่สำเร็จ")
#22
num = random.choice([123,321])
print(num,"ตัวแรกมากกว่าตัวที่สอง" if str(num)[0] > str(num)[1] else "ไม่")
#23
num = rd(6,18)
print(num,"คู่และมาก" if num % 2 == 0 and num > 10 else "ไม่")
#24
num = rd(0,100)
print(num,"ตก" if num <= 40 else "ผ่าน")
#25
name = random.choice(["FEW","few"])
print(name,"ตัวใหญ่" if str(name).isupper() else "ตัวเล็ก")
#26
num = rd(0,400)
print(num,"ช่วงกลาง" if 100 < num < 200 else "ไม่")
#27
num = rd(0,100)
print(num,"ระดับ A" if 80 < num < 100 else "ไม่")
#28
name = random.choice(["M","F"])
print(name,"ชาย" if name == "M" else "หญิง")
#29
name = random.choice(["admin","not admin"])
print(name,"ยินดีต้อนรับแอดมิน" if name == "admin" else "ไม่")
#30
day = {"จันทร์":"ทำงาน","อังคาร":"ทำงาน","พุธ":"ทำงาน","พฤหัสบดี":"ทำงาน","ศุกร์":"ทำงาน","เสาร์":"หยุด","อาทิตย์":"หยุด"}
r = random.choice([i for i in day])
print(r,day[r])
#31
num1,num2,num3,m = rd(0,100),rd(0,100),rd(0,100),0
if num1 >= m: m = num1
if num2 >= m: m = num2
if num3 >= m: m = num3
print(num1,num2,num3,m)
#32 ###############################
num = rd(0,2025)
print(num)
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0): print(num,"true")
else: print(num,"false")
#33
import datetime
# print(datetime.time(20,10).strftime("%H:%M"))

# time = input("time : ")
time = "02:01"
time = int(time[:2])
if time >= 6 and time <= 11: print("เช้า")
elif time >= 12 and time <= 17: print("บ่าย")
elif time >= 18 and time <= 23: print("เย็น/ค่ำ")
else: print("ดึก")
#34
mess = ""
for i in range(3):
    num = int(input(f"point{i} : "))
    if num >= 50: mess = "ผ่าน"
    else:
        mess = "ไม่ผ่าน"
print(mess)