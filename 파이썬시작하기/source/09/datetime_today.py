from datetime import datetime

today = datetime.now()
print(type(today))

print('%s년' % today.year)
print('%s월' % today.month)
print('%s일' % today.day)
print('%s시' % today.hour)
print('%s분' % today.minute)
print('%s초' % today.second)

today_str = today.strftime('%Y/%m/%d %H:%M:%S')

print(today_str)




