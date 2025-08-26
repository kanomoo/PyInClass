# import math
# print()
# print("=" * 40)
# print("|Angle|   Sin    |   Cos    |  Tan     |")
# print("=" * 40)
# for angle in range(0, 361, 20):
#     radian = math.radians(angle)
#     print(f"|%4d |" % angle,end="")
#     print("%9.5f |" % math.sin(radian),end="")
#     print("%9.5f |" % math.cos(radian),end="")
#     print("%9.5f |" % math.tan(radian))
# print("=" * 40)

# import math
# head = "|Angle|   Sin    |   Cos    |   Tan    |"
# line = len(head) * "="
# print(line,head,line,sep="\n")
# for i in range(0,361,20):
#     r = math.radians(i)
#     print(f"|{i:4} |{math.sin(r):9.5f} |{math.cos(r):9.5f} |{math.tan(r):9.5f} |")
# print(line)