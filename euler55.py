'''
How many Lychrel numbers are there below ten-thousand?
'''
lch = []
for x in range(1, 10000):
	n = x
	lch_num = True
	for y in range(50):
		n = n + int(str(n)[::-1])
		if str(n)==str(n)[::-1]:
			lch_num=False
			break
	if lch_num:
		lch.append(x)
		
		
print(len(lch))