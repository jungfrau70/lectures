def isValid(p) : 
   if len(p) < 10 : 
      return False 

   is_num = False 
   is_upper = False 

   for ch in p : 
      if ch >= 'A' and ch <= 'Z' : 
         is_upper = True 
      if ch >= '0' and ch <= '9' : 
         is_num = True 

   return is_upper and is_num 


print('※ 비밀번호는 10자리 이상, 숫자와 영문 대문자로 구성되어야 합니다.') 

password = input('비밀번호 : ') 

while not isValid(password) : 
   print(' 비밀번호가 잘못되었습니다(10자리 이상, 영문 대문자 포함)! 다시 입력해 주세요!') 
    
   password = input('비밀번호: ') 

print(' 유효한 비밀번호입니다~~~')
