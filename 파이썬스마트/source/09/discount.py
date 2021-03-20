price = int(input('물건 구매가를 입력하세요 : ')) 

if price >= 5000 and price < 10000 : 
   rate = 5.0 
elif price >= 10000 and price < 50000 : 
   rate = 7.5 
elif price >= 50000 : 
   rate = 10.0 
else : 
   rate = 0 
    
pay = price - (price * rate)/100 

print('구매가 : %.0f' % price) 
print('지불 금액 : %.0f' % pay)

