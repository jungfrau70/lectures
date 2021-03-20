a = int(input("성적을 입력하세요(종료 시 -1 입력) : "))

scores = []

while a != -1 :
    scores.append(a)
    a = int(input("성적을 입력하세요(종료 시 -1 입력) : "))

sum = 0
for score in scores :
    sum = sum + score

avg = sum/len(scores)
print("입력된 성적 : ", scores)
print("평균 : %.2f" % avg)
