pilgi = int(input('필기시험 점수를 입력하세요 : '))
silgi = int(input('실기시험 점수를 입력하세요 : '))

if pilgi >= 80 and silgi >= 80 :
    result = '합격'
else :
    result = '불합격'

print('- 필기시험 점수 : %s' % pilgi)
print('- 실기시험 점수 : %s' % silgi)
print('- 판정 : %s' % result)
