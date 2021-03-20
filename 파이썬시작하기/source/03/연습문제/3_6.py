userid = input('아이디를 입력하세요 : ') 

if userid == 'admin' :
    print('해당 콘텐츠 이용이 가능합니다!')    
else  :
    level = int(input('회원 레벨을 입력해 주세요 : '))
    
    if  level>=1 and level<=7 :
        print('해당 콘텐츠 이용이 가능합니다!')
    else  :
        print('해당 콘텐츠에 접근할 수 없습니다. 관리자에게 문의해 주세요!')
