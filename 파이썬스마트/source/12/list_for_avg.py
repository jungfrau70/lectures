scores = [ 80, 92, 99, 75, 87]
sum = 0

for s in scores :
    sum = sum + s
    print("점수 : %d, 누적 합계 : %d" % (s, sum))
    
avg = sum/len(scores)

print("\n합계 : %d, 평균 : %.2f" % (sum, avg))
    
