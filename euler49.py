'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''


import math
primes=[]

def get_primes(mx):
	x=1
	while x < mx:
		x+=1
		y=int(math.sqrt(x))
		isprime=True
		for z in primes:
			if z > y:
				break
			if x%z==0:
				isprime=False
				break
		if isprime:
			primes.append(x)
			
			
get_primes(10000)
print(primes[-1])


primes = [x for x in primes if x > 999]
print(len(primes))


for i, x in enumerate(primes):
	for y in primes[i+1:]:
		if y + y - x in primes and set(str(x)) == set(str(y)) == set(str(y+y-x)):
			print(x, y, y + y - x)