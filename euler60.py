#pylint:disable=E0001
#pylint:disable=E0001
'''
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
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

p=[]
for x in primes:
	if x > 1500:
		break
	p.append(x)

def check_concat_primes(p):
	res = True
	last = p[-1]
	rem = p[:-1]
	#pairs = [(x[0], x[1]) for x in itertools.permutations(p, 2) if last in x and x[0] != x[1]]
	
	
	for y in rem:
		pairs = [(y, last), (last, y)]
		for x in pairs:
			item = str(x[0]) + str(x[1])
			if not int(item) in pr_dict[len(item)]:
			#print(int(str(x[0]) + str(x[1])), ' not a prime')
				res = False
				break
	return res
			
print(len(p))
import itertools
combs = list(itertools.combinations(p, 2))
print(len(combs))
two_pairs =[]
for s in combs:
	#print(s)
	if s[0] != s[1] and check_concat_primes(s):
		#print(s, sum(s))
		#break
		two_pairs.append(s)
print(len(two_pairs))
#908
three_pairs = []
for x, y in itertools.product(two_pairs, p):
	s = (x[0], x[1], y)
	if y not in x and check_concat_primes(s):
		three_pairs.append(s)
print(len(three_pairs))
#723

four_pairs = []
for x, y in itertools.product(three_pairs, p):
	s = (x[0], x[1], x[2], y)
	if y not in x and check_concat_primes(s):
		four_pairs.append(s)
print(len(four_pairs))
#24

five_pairs = []
for x, y in itertools.product(four_pairs[:100], p):
	s = (x[0], x[1], x[2], x[3], y)
	if y not in x and check_concat_primes(s):
		five_pairs.append(s)
print(len(five_pairs))

if len(five_pairs):
	print(five_pairs[0])
#0
#print(check_concat_primes([3, 7, 109, 673]))


