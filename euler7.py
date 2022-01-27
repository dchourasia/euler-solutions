'''
What is the 10 001st prime number?
'''

n = 10001

primes=[]
i = 2
primeten = []
primehundred=[]
while len(primes) < n:
	if len(primes)==10:
		primeten= primes.copy()
	
	if len(primeten):
		div = list(filter(lambda x: i%x == 0, primeten))
		if len(div)!=0:
			i += 1
			continue
			
	if len(primes)==100:
		primehundred= primes.copy()
	
	if len(primehundred):
		div = list(filter(lambda x: i%x == 0, primehundred))
		if len(div)!=0:
			i += 1
			continue
			
	div = list(filter(lambda x: i%x == 0, primes))
	if len(div) == 0:
		primes.append(i)
	i += 1

#print(primes)
#print(n*(n+1)/2)
print(primes[-1])