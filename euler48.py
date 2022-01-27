'''
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
'''
size = 1000
import math
sm = 0
for n in range(1, size + 1):
	#print(n)
	#sm += int(str(int(math.pow(n, n)))[:10])
	p=1
	for x in range(size):
		p *= size
		p = int(str(p)[:11])
	sm += p
	a=1

print(str(sm)[-10:])
#print(math.pow(1.43, 143))

#12 x 37
# 84