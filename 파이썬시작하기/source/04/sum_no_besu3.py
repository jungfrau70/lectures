
sum = 0

for i in range(300, 901) :
    if i % 3 != 0 :
        sum = sum + i
    
print('300과 900까지의 정수 중 3의 배수가 아닌 수의 합계 : %d' % (sum))

