price = int(input('물건 가격 : ')) 
num = int(input('구매 개수 : ')) 
pay = int(input('지불 금액 : ')) 

change = pay - price * num 

print('물건 가격 : %d, 구매 개수 : %d, 지불 금액 : %d => 거스름 돈 : %d ' % (price, num, pay, change)) 
