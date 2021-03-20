i = 1
sum = 0

while True :
    if i > 10 :
        break

    sum = sum + i
    print('sum = %2d, i = %2d' % (sum, i))
        
    i = i + 1

print('\n합계 : %d' % sum)
