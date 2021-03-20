pilgi = int(input("필기 점수를 입력하세요! "))
silgi = int(input("실기 점수를 입력하세요! "))

result = "불합격!"

if pilgi >= 70 and silgi >= 80 :
    result = "합격!"

print(result) 
