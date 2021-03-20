month = int(input('월을 입력해주세요 : ')) 

if month >= 3 and month <= 5 : 
   season = '봄' 

   print(month, '월은 ', season, '입니다', sep='') 
elif month >= 6 and month <= 8 : 
   season = '여름' 
   print(month, '월은 ', season, '입니다', sep='') 
elif month >= 9 and month <= 11 : 
   season = '가을' 
   print(month, '월은 ', season, '입니다', sep='') 
elif month == 12 or month == 1 or month == 2 : 
   season = '겨울' 
   print(month, '월은 ', season, '입니다', sep='') 
else  : 
   print('월이 잘못 입력되었습니다!')
