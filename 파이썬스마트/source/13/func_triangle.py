def triangle(a, b) :
    c = a * b * (1/2)
        
    return c

length = int(input("삼각형의 밑변의 길이를 입력하세요 : "))
height = int(input("삼각형의 높이를 입력하세요 : "))

area = triangle(length, height)
             
print("밑변의 길이 : %d cm, 높이 : %d cm" % (length, height))
print("삼각형의 면적 : %.2f cm2" % area)
