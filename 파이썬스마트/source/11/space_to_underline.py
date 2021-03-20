string = input("문장을 입력하세요 : ")

for i in string :
    if i == " " :
        print("_", end="")
    else :
        print(i, end="")
    
