a = int(input('첫 번째 수를 입력하세요: '))
b = int(input('두 번째 수를 입력하세요: '))

c = a + b
d = b + a

if c == d :
    print('%d + %d의 결과 : %d' % (a, b, c))
    print('%d + %d의 결과 : %d' % (b, a, d))
    print('덧셈의 교환법칙이 성립합니다.')
else :
    print('a + b의 결과 : %d' % c)
    print('b + a의 결과 : %d' % d)
    print('덧셈의 교환법칙이 성립하지 않습니다.')

