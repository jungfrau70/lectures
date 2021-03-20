def barDecrypt(code) : 
    if code == '||:::' : 
        num = '0' 
    elif code == ':::||' : 
        num = '1' 
    elif code == '::|:|' : 
        num = '2' 
    elif code == '::||:' : 
        num = '3' 
    elif code == ':|::|' : 
        num = '4' 
    elif code == ':|:|:' : 
        num = '5' 
    elif code == ':||::' : 
        num = '6' 
    elif code == '|:::|' : 
        num = '7' 
    elif code == '|::|:' : 
        num = '8' 
    else :  
        num = '9' 
    return num 

loop = True 
in_string = input('바코드를 입력하세요: ') 

num = ''
for i in range(0, len(in_string), 5) : 
    num = num + barDecrypt(in_string[i:i+5])

print(num)
