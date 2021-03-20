def check_password(p) :
    answer = '12345'
    
    if p == answer :
        result = True
    else :
        result = False
                
    return result

password = input("비밀번호를 입력하세요 : ")

if check_password(password) :
    print("비밀번호가 맞습니다!")
else :
    print("비밀번호가 틀렸습니다!")
