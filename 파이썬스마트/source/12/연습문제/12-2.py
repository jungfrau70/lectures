scores = [65, 78, 55, 38, 98, 88, 77, 64, 100, 80,
          85, 98, 59, 99, 68, 87, 99, 46, 85, 93,
          85, 98, 59, 99, 68, 87, 99, 46, 85, 93,
          67, 99, 63, 79, 92, 80, 68, 62, 96, 84]

i = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

while i < len(scores) :
    if scores[i] >= 90:
        num1 = num1 + 1
    elif scores[i] >= 80: 
        num2 = num2 + 1
    elif scores[i] >= 70: 
        num3 = num3 + 1
    elif scores[i] >= 60: 
        num4 = num4 + 1
    else :
        num5 = num5 + 1

    i = i + 1

print("-"*50)
print("%10s %11s" % ("점수", "인원"))
print("-"*50)

print("%12s %8d명" % ("90점 이상", num1))
print("%12s %8d명" % ("80점 이상", num2))
print("%12s %8d명" % ("70점 이상", num3))
print("%12s %8d명" % ("60점 이상", num4))
print("%12s %8d명" % ("60점 미만", num5))

print("-"*50)
print("%10s %9d명" % ("전체인원", len(scores)))
print("-"*50)

