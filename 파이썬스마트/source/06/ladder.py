top = float(input("사다리꼴 윗변의 길이를 입력하세요! "))
bottom = float(input("사다리꼴의 밑변의 길이를 입력하세요! "))
height = float(input("사다리꼴의 높이를 입력하세요! "))

area = ( (top + bottom) * height ) / 2

print("사다리꼴의 면적 : %.1f cm2" % area)
