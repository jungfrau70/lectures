def cal(a, b, mode) :       
    if mode == 1 :
        print('%d + %d = %d' % (a, b, a + b))
                
    if mode == 2 :
        print('%d * %d = %d' % (a, b, a * b))                

    if mode == 3 :
        print('%d - %d = %d' % (a, b, a - b))
                
cal(10, 20, 1)
cal(30, 40, 2)
cal(200, 500, 3)
