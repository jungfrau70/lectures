
print('-' * 50) 
print('%7s \t %7s \t %7s' % ('달러($)', '원화(원)', '유로(€)'))
print('-' * 50) 

dollar = 10

while dollar <= 100 : 
    won  = dollar * 1080
    euro = dollar * 0.81

    print('%7d \t %8.0f \t %7.1f' % (dollar, won, euro))   

    dollar = dollar + 10
    
print('-' * 50)

