'''
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
import datetime

count = 0
for x in range(1901, 2001):
	for y in range(1, 13):
		d = datetime.datetime(x, y, 1)
		if d.weekday() == 6:
			count += 1
			
			
			
print(count)