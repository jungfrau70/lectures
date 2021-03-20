num_writing = int(input("글쓴 개수를 입력하세요 : "))
num_ripple = int(input("댓글 단 개수를 입력하세요 : "))

if num_writing >= 5 and num_ripple >= 10 :
    level = 7
else :
    level = 9
 
print("- 글쓴 개수 : %d, 댓글 개수 : %d" % (num_writing, num_ripple))
print("- 회원 레벨 : %d" % level)

    
