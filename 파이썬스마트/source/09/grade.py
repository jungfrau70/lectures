score = int(input("점수를 입력하세요: "))

if score >= 90 :
   grade = "수"
elif score >= 80 :
   grade = "우"
elif score >= 70 :
   grade = "미"
elif score >= 60 :
   grade = "양"   
else :
   grade = "가"   

print("등급 : %s" % grade)
