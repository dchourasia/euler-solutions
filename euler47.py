'''
The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
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
			
			
get_primes(1000000)
print(primes[-1])

def get_factors(n):
	factors = []
	if n in primes:
		return [n]
		
	for f in primes:
		if n == 1:
			break
		if n%f == 0:
			factors.append(f)
			n = int(n/f)
			while n%f == 0:
				n = int(n/f)
				
				
	return factors
	
	
#print(get_factors(99))
facts={}
pr_count=0
for x in range(100000, 500000):
	f = get_factors(x)
	if len(f) == 4:
		pr_count += 1
		#print('yes', x)
	else:
		pr_count = 0
		
	if pr_count == 4:
		print(x-3)
		break
	
				
				
				
			