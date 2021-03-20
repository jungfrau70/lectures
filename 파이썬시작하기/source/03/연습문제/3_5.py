buy = int(input('물건 구매가를 입력하세요 : ')) 

if buy >= 10000 and buy < 50000 : 
   rate = 5.0 
elif buy >= 50000 and buy < 300000 : 
   rate = 7.5 
elif buy >= 300000 : 
   rate = 10.0 
else : 
   rate = 0 
    
discount = buy * rate / 100 
pay = buy - discount 

print('구매가 : %.0f' % buy) 
print('할인율 : %.1f%%' % rate) 
print('할인 금액 : %.0f' % discount) 
print('지불 금액 : %.0f' % pay)
