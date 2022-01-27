'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''


import math

n = 1000000
primes= []

def isprime(i):
	
	isprime = True
	max = int(math.sqrt(i))
	
	for y in primes:
		if i%y == 0:
			isprime= False
			break
		if y > max:
			break
		
	return isprime
	
def get_rotations(n):
	rots = []
	n = str(n)
	for x in range(len(n)):
		n = n[-1:] + n[:len(n)-1]
		rots.append(int(n))
	#print(rots)
	
	return set(rots)
		
	
res = [primes.append(x) for x in range(2, n) if isprime(x)]
primes=set(primes)
circ_primes = [p for p in primes if get_rotations(p).issubset(primes)]
print(len(primes))
#get_rotations(2)

print(len(circ_primes))