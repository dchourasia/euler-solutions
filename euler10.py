'''
Find the sum of all the primes below two million.
'''
import math

n = 2000000
primes= []

def isprime(x):
	isprime = True
	max = int(math.sqrt(x))
	for y in primes:
		if x%y == 0:
			isprime= False
			break
		if y > max:
			break
		
	return isprime
	div = [y for y in primes if x%y == 0]
	return not len(div)
	
	
res = [primes.append(x) for x in range(2, n) if isprime(x)]

#print(primes)
print(sum(primes))

x=99
#print(int(math.sqrt(x)))
#print(primes[0 if x%2 == 0 else 1:None if 13 not in primes else primes.index(13)])
#print(min(range(len(primes)), key=lambda i: abs(primes[i]-9)))