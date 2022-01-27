'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
import itertools, math
mx = 200
pr_map = {}
odds = [x for x in range(3, mx) if x%2==1]
#print(odds)

comps = [x*y for x, y in itertools.product(odds,odds)]

print(len(comps), max(comps))

primes=[]
size=1000

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
		else:
			pr_map[x] = primes[::-1]
			
			
get_primes(10000)
#print(primes)
			
goldbach=[]
comps=sorted(list(set(comps)))
#print(comps)

for x in comps:
	isgb=False
	for y in pr_map[x]:
		#if y >= x:
			#break
		d=(x-y)/2
		#print(d)
		
		if d - math.floor(d) > 0:
			continue
		sr = math.sqrt(d)

		if sr - math.floor(sr) == 0:
			#print(x, y)
			isgb=True
			goldbach.append(x)
			break
	if not isgb:
			print(x)
			break
			
			
#print(goldbach)
			
	