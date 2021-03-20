scores = []

while True :
    score = int(input('성적을 입력하세요(종료 시 -1 입력): '))

    if score == -1 :
        break
    else :
        scores.append(score)

print('%s' % scores)

