'''
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
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
print(len(primes))
s= len(primes)
det={}
for p in primes[s-1:s-10:-1]:
	#all = [primes[x:y] for x in range(s) for y in range(x+100, s) if sum(primes[x:y]) == p]
	all = []
	for x in range(s):
		for y in range(x+50, s):
			if sum(primes[x:y]) == p:
				all =[primes[x:y]]
				break
	if len(all):
		mx = max(all, key=len)
		print(mx)
		print(p, len(mx))
		det[p]=len(mx)
		#break
mx = max(det, key=lambda x: det[x])
print(mx, det[mx])

	