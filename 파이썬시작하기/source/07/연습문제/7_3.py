def cir_area(radius) :
    area = radius * radius * 3.14
    return area

def cir_circum(radius) :
    circum = 2 * 3.14 * radius
    return circum

r = float(input('반지름을 입력하세요: '))
a = cir_area(r)
b = cir_circum(r)
print('원의 면적 : %.2f, 원주의 길이 :%.2f' % (a, b))
