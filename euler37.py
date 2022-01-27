'''
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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
	
def get_truncations(n):
	truncs = []
	n = str(n)
	for x in range(len(n)):
		truncs.append(int(n[:len(n)-x]))
		truncs.append(int(n[x:]))
		
	
		#print(truncs)
	
	return set(truncs)
		
	
res = [primes.append(x) for x in range(2, n) if isprime(x)]
primes=set(primes)
circ_primes = [p for p in primes if p > 10 and get_truncations(p).issubset(primes)]
#print(len(primes))
#get_truncations(3797)

print(circ_primes)
print(sum(circ_primes))
