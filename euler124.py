'''
If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
'''

import math
primes=[]
pdict = {}

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
		pdict[x] = len(primes)
			
get_primes(100000)
print(primes[-1])

rads ={1:1}

def get_rad(x):
	prs = primes[:pdict[x]]
	if x == prs[-1]:
		return x
	rad = 1
	for n in prs:
		if x%n == 0:
			rad *= n
			#print(n)
			while x%n == 0:
				x = x/n
			return n*rads[x]
			
		#if x == 1:
			#break
	#print(rad)
	#return rad
			
	
for n in range(2, 100001):
	rads[n] = get_rad(n)
	
k = sorted(rads, key=lambda x: (rads[x], x))

#rads = {x:rads[x] for x in k}
'''
print(len(rads))
key = list(rads.keys())[9999]
print(key, rads[key])
'''	
for idx, v in enumerate(k):
	print(v, rads[v])	
	if idx>20:
		break

print(k[9999], rads[k[9999]])
#get_rad(12)
