sentence =  input("영어 문장을 입력해 주세요 : ")

count = 0
print("모음 : ", end = "")

for i in sentence :
    if ( i == "a" or i == "A"  or i == "e" or i == "E" \
        or  i == "i" or i == "I" or i== "o" or i == "O" \
        or i == "u" or i == "U") :
        count = count + 1
        print(i, end=" ")
        
print("\n모음의 개수 : %d" % count)
