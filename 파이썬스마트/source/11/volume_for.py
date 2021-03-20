print("-" * 30)
print("%6s %6s %6s" % ("리터", "갤런", "온스"))
print("-" * 30)

for litter in range(1, 51, 2) :
    gallon = litter * 0.264
    ounce  = litter * 33.814   
    print("%8.2f %8.2f %8.2f" % (litter, gallon, ounce))

print("-" * 30)
