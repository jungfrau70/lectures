def computeMinGong(x, y):
   if x > y :
       big = x
   else:
       big = y

   while(True):
      if((big % x == 0) and (big % y == 0)):
         result = big
         break
      big = big + 1

   return result

num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))

min_gong = computeMinGong(num1, num2)

print('%d와 %d의 최소공배수 : %d' % (num1, num2, min_gong))
