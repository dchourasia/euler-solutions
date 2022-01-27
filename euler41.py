'''
What is the largest n-digit pandigital prime that exists?
'''
import math, itertools

n = 100000
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
	
def is_pand(n):
	return '0' not in str(n) and len(str(n)) == len(set(str(n)) )
		
	
res = [primes.append(x) for x in range(2, n) if isprime(x)]

mx=0

combs =[]
for y in range(9, 6, -1):
	st = ''.join(map(str, range(1, y+1)))
	combs += [int(''.join(x)) for x in itertools.permutations(st)]
	
#print(combs)
pan_primes = []
for mx in combs:
	if is_pand(mx) and isprime(mx):
		pan_primes.append(mx)

	
print(pan_primes)
print(max(pan_primes))


