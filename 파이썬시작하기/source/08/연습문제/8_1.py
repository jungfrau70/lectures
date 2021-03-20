class Fruit :
    name = '오렌지'
    color = '노란색'
    def taste(self) :
        print('새콤하다.')

    def vitamin(self) :
        print('비타민 C가 풍부하다.')
    

orange = Fruit()

print('과일명 : %s' % orange.name)
print('색상 : %s' % orange.color)
orange.taste()
orange.vitamin()








