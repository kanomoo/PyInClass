amount = int(input("Enter amount : ")) #รับตัวเลขจำนวนเต็มที่เป็นamountเข้ามาเก็บไว้ที่ตัวแปรamount
rate = float(input("Enter rate : ")) #รับตัวเลขทศนิยมที่เป็นข้อมูลrateเข้ามาเก็บไว้ที่ตัวแปรrate
year = int(input("Enter year : ")) #รับตัวเลขที่เป็นข้อมูลyearเข้ามาเก็บไว้ที่ตัวแปรyear
num = amount*(1 + (rate/100))**year #คำนวณจากสูตรที่ได้รับมาและนำค่าที่ได้ไปเก็บไว้ที่num
print(num) #แสดงค่าที่คำนวณได้