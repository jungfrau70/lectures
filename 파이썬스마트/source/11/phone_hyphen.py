phone_numbers = input("하이픈(-)을 포함하여 전화번호를 입력하세요 : ")

for i in phone_numbers :
    if i!="-" :
        print(i, end="")
    
