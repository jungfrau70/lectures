def maxTwo(i, j):
    if i > j:
        return i
    else :
        return j

def maxThree(x, y, z) :
    return maxTwo( maxTwo(x, y), maxTwo(y, z))

a = int(input('첫 번째 수를 입력하세요: '))
b = int(input('두 번째 수를 입력하세요: '))
c = int(input('세 번째 수를 입력하세요: '))

max_num = maxThree(a, b, c)

print('%d, %d, %d 중 가장 큰 수 : %d' % (a, b, c, max_num))
