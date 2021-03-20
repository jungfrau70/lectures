scores = [ 80, 92, 99, 75, 87]
i = 0
sum = 0

while i <len(scores) :
    sum = sum + scores[i]
    print("점수 : %d, 누적 합계 : %d" % (scores[i], sum))
    i = i + 1
    
avg = sum/len(scores)
print("\n합계 : %d, 평균 : %.2f" % (sum, avg))
    
