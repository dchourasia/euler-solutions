'''
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
'''

a, b, c, d= 1, 1, 3, 2
res = []
for n in range(1, 1000):
	y = 2*d + b
	x = y + d
	#print(x, y)
	if len(str(x)) > len(str(y)):
		res.append((x, y))
	a, b, c, d = c, d, x, y

print(len(res))

