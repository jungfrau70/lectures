def sum_besu3(n) :
    sum = 0
    for i in range(1, n+1) :
        if i % 3 == 0 :
            sum = sum + i

    return sum

num = int(input('양의 정수를 입력하세요: '))
result = sum_besu3(num)

print('1 ~ %d까지의 정수 중 3의 배수의 합 : %d' % (num, result))





