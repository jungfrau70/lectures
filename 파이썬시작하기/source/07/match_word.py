def matchWord(in_word, answer) : 
   if in_word == answer : 
      msg = '참 잘했어요~~~' 
   else : 
      msg = '단어 공부 좀 더 해야겠어요.ㅋㅋ' 
   return msg 

eng_dict = {'apple':'사과', 'lion':'사자', 'book':'책', 'love':'사랑', 'friend':'친구'} 

for i in eng_dict : 
    string = input(eng_dict[i] + '에 맞는 영어 단어는? ') 
    result = matchWord(string, i) 
    print(result)



