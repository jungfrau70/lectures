def reverse(char) :
    length = len(char)
    string = ""
    for i in range(length-1, -1, -1) :
        string = string + char[i]

    return string

data = input("문장을 입력하세요 : ")
print(reverse(data))

