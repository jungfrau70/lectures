count = 0
sum = 0

for i in range(201) : 
    if i % 3 == 0 : 
        sum = sum + i
        print("%6d" % sum, end="")
        count = count + 1
        
        if count % 10 == 0 : 
            print()
            
     
 
