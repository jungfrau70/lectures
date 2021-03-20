print("-" * 30)
print("%8s %8s" % ("화씨", "섭씨"))
print("-" * 30)

f = 0

while f <= 100 :
    c = (f - 32) / 1.8    
    print("%10.2f %10.2f" % (f, c))
    f = f + 10

print("-" * 30)

