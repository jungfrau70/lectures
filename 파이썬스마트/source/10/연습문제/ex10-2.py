print("=" * 50)
print("%12s %5s %8s" % ("킬로미터", "마일", "야드"))
print("=" * 50)

km = 10

while km <= 200 :
    mile = km * 0.621371
    yd = km * 1093.6133
    
    print("%12d %12.2f %12.2f" % (km, mile, yd))
    
    km = km + 10

print("=" * 50)
