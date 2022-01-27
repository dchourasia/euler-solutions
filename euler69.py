'''
Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''
import math
primes=[]
phi = {}
def get_primes(mx):
	x=1
	for a in range(2, mx):
		#x+=
		x = a
		ph = x - 1
		y=int(math.sqrt(x))
		isprime=True
		for z in primes:
			if z > y or int(x) == 1:
				break
			if x%z==0:
				isprime=False
				while x%z == 0:
					x /= z
					ph -= 1
				#break
		if isprime:
			primes.append(x)
		phi[a] = ph
			
			
get_primes(20)
print(phi)

def phi_org(n):
	res = n
	i = 2
	while i*i <= n:
		if n %i == 0:
			while n%i == 0:
				n /= i
			res -= res/i
		i += 1
	if n > 1:
		res -= res/n
	return res

def phi_new(x):
	if x in primes:
		return x - 1