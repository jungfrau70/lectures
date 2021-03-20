person1 = input("첫 번째 사람의 이름을 입력하세요! ")
h1 = int(input("첫 번째 사람의  키를 입력하세요! "))
person2 = input("두 번째 사람의 이름을 입력하세요! ")
h2 = int(input("두 번째 사람의  키를 입력하세요! "))

name = person1
height = h1


if h2 > height :
    name = person2
    height = h2 

print("키가 큰 사람의 이름 : %s, 키 : %d" % (name, height))
 
