month = int(input("월을 입력하세요: "))

if month == 2 :
   print("28일 또는 29일까지 있어요!")
elif month == 4 or month == 6 or month == 9 or month == 11 :
   print("30일까지 있어요!")
else :
   print("31일까지 있어요!")
