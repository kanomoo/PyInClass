from random import uniform
uniform1 = round(uniform(30,50),2) #ใช้ uniform เพื่อหาค่าสุ่มตัวเลขที่มีทศนิยม แล้วใช้ round เพื่อกำหนดทศนิยม 2 ตำแหน่ง
uniform2 = round(uniform(30,50),2) #ต้องสร้างหลายตัวเพราะสุ่มหลายค่า
uniform3 = round(uniform(30,50),2)
uniform4 = round(uniform(30,50),2)
uniform5 = round(uniform(30,50),2)
total = round(uniform1 + uniform2 + uniform3 + uniform4 + uniform5,2)
print("Value random :",uniform1,",",uniform2,",",uniform3,",",uniform4,",",uniform5)
print("Total value :",total)
print("Average value :",round((total / 5),2))
