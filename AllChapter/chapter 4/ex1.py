import math
print("Equation 1 : sin x ^2 + cos x ^ 2")
x = float(input("Enter value x (degree angle) : "))
print("x =",x) #56.4
print("value of sin x ^2 + cos x ^ 2 is",format(pow(math.sin(x),2) + pow(math.cos(x),2),".8f")) #ต้อง format เพื่อให้มีทศนิยม 8 ตำแหน่ง

print("\nEquation 2 : e^(0.5 sqrt( tan cos x ) )")
x = float(input("Enter value x (degree angle <= 90) : "))
print("x =",x) # 23.7
x = math.radians(x) # math.cos tan ต้องการค่ามุมในหน่วยเรเดียน radians
print("value of   e^(0.5 sqrt( tan cos x ) ) is",math.exp(1/2 * math.sqrt(math.tan(math.cos(x)))))

print("\nEquation 3 : [ log(x^2/(1-x)) ] / [ x^(5+x) ]")
x = float(input("Enter value x (0.0 - 1.0 ) : "))
print("x =",x) # 0.345  #log ธรรมดาเป็นฐาน e natural logarithm  ต้องใช้ log ฐาน 10
print("value of [ log(x^2/(1-x)) ] / [ x^(5+x) ] is",math.log10(pow(x,2) / (1-x)) / (pow(x,5+x)))