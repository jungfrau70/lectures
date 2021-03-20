price = int(input("물건 가격을 입력하세요 : "))
num = int(input("구매 개수를 입력하세요 : "))

buy = price * num

if buy >= 50000 :
    delivery = 0
elif buy <= 50000 and buy >= 30000 :
    delivery = 2000
else :
    delivery = 5000

payment = buy + delivery

print("구매 금액 : %d원, 배송료 : %d원, 결제 금액 : %d" % (buy, delivery, payment))
