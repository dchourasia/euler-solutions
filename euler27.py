import math, time


t1 = time.time()

n = 20000
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
	
	
	
res = [primes.append(x) for x in range(2, n) if isprime(x)]

#print(max(primes))
counts = {}
r = 1000

for x in range(-r, r):
	for y in range(-r, r):
		cnt=0
		n=0
		prime = n*n + x*n + y
		while prime in primes:
			cnt += 1
			n += 1
			prime = n*n + x*n + y
		counts[(x, y)] = cnt
		
		
print(max(counts, key=counts.get))
			

t2 = time.time()

print('elapsed', t2 - t1)