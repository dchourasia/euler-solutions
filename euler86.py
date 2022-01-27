



import math
primes=[]
pr_dict = {}
for i in range(1, 20):
	pr_dict[i] = []

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
			pr_dict[len(str(x))].append(x)
			
			
get_primes(2000000)
print(primes[-1])