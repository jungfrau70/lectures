sum = 0

for i in range(500, 1001) :
    if i % 7 == 0 :
        print(i)
        sum = sum + i

print("합계 : %d" % sum)
    
