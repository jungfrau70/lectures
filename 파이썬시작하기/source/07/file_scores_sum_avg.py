file = open('scores.txt', 'r')
lines = file.readlines()
file.close()

print(lines)
print('-' * 50)

for line in lines :
    student = line.split()
    i = 0
    sum = 0
    while i<6 :
        if i == 0 :
            print(student[i])
        else :
            sum = sum + int(student[i])

        i = i + 1
    print('합계 : %d, 평균 : %.2f' % (sum, sum/5))
    print('-' * 50)







