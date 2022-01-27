'''
what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''
#br = 2(2n + 1) + 2(2(n - 1) + 1) - 2 == 8n -2
#1	7	21	43
#	6	14	22
#side = 2n + 1
#br = sqr(2n + 1)
#tl = 3(2n +1) + (2(n-1) + 1) -2 == 8(2n + 1)/2
#tr = 8n - (2n -1) + (2n + 3) - 1 == 8n + 2
#4(2n+1) - 4 = 8n (perimeter length)
#


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
			
			
get_primes(10000000)
print(primes[-1])
primes = set(primes)
def get_perc_primes(x):
	x = set(x)
	prs = x & primes
	#print(prs, len(x))
	return len(prs)*100/len(x)
	
bl = [1]
br = [1]
tl = [1]
tr = [1]
diag = {}

for n in range(1, 2000):
	bl.append(bl[n-1] + 8*n - 2)
	br.append((2*n+1)*(2*n+1))
	tl.append(tl[n-1] + 4*(2*n - 1))
	tr.append(tr[n-1] + 8*n - 6)
	diag[n] = bl + br + tl + tr
print(max(br))

for n in range(1000, 1500):
	x = get_perc_primes(bl + br + tl + tr)
	print(x)
	#if x < 10:
		#print(2*n+1)
		#print(x)
		#break

#print(bl, br, tl, tr)
