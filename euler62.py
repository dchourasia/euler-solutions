'''
Find the smallest cube for which exactly five permutations of its digits are cube.
'''
import math, itertools
print(math.pow(8, 1/3).is_integer())
tried = {}
for i in range(1000, 1200):
	cb = int(math.pow(i, 3))
	#print(cb)
	#print(math.pow(int(cb), 1/3))
	roots = 1
	tried[i] = [str(cb)]
	for x in itertools.permutations(str(cb)):
		x = ''.join(x)
		if x not in tried[i]:
			#print('x =', x)
			y = round(math.pow(int(x), 1/3))
		#print(y**3, x)
			if y**3 == int(x):
				roots += 1
				tried[i].append(x)
				print(roots, i, y, x)
	if roots == 5:
		print(cb)
		break
	
		