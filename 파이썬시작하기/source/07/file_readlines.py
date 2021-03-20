file = open('scores.txt', 'r')
lines = file.readlines()

print(lines)

for line in lines :
	print(line, end='')
    
file.close()






