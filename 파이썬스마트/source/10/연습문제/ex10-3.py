pound = int(input("파운드를 입력하세요(종료:-1) : "))

while True :
    if pound != -1 :
        kg = pound * 0.453592
        print("%d 파운드(lb)는 %.2f 킬로그램(kg)입니다." % (pound, kg))
        pound = int(input("파운드를 입력하세요(종료:-1) : "))
    else :
        break

print("프로그램이 종료되었습니다!")
