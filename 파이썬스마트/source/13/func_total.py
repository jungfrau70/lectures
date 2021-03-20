def total(start, end) :
    sum = 0
    for i in range(start, end+1) :
        sum = sum + i
        
    return sum

print(total(1, 10))
print(total(200, 300))
print(total(5000, 8000))
    
