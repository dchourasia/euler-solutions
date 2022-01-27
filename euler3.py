'''
What is the largest prime factor of the number 600851475143 ?
'''

n = 600851475143

primes=[]
p = 2

while n> 1:
	multiplesof = list(filter(lambda x: p%x == 0, primes))
	isprime = len(multiplesof) == 0
	if isprime and n%p == 0:
		primes.append(p)
		while n%p == 0:
			n = n/p
	p += 1
	
print(primes)
print(max(primes))
