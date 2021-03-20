def even_odd(n) :
    if n % 2 == 0 :
        result = "짝수"
    else :
        result = "홀수"

    return result

num = int(input("자연수를 입력하세요 : "))

print("%d => %s" % (num, even_odd(num)))



    
