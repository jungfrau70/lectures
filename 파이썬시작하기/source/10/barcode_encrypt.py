def barEncrypt(n) :
    if n == '0' : 
        code = '||:::' 
    elif n == '1' : 
        code = ':::||' 
    elif n == '2' : 
        code = '::|:|' 
    elif n == '3' : 
        code = '::||:' 
    elif n == '4' : 
        code = ':|::|' 
    elif n == '5' : 
        code = ':|:|:' 
    elif n == '6' : 
        code = ':||::' 
    elif n == '7' : 
        code = '|:::|' 
    elif n == '8' : 
        code = '|::|:' 
    elif n == '9' : 
        code = '|:|::'
    else :
        code = '?????'

    return code 

loop = True 
while loop : 
    in_string = input('5~10 자리 숫자를 입력하세요: ') 
    if len(in_string) >=5 and len(in_string) <=10 : 
            break 

string = '' 
for i in list(in_string) : 
      string = string + barEncrypt(i) 

print(string)
