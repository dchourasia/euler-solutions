'''
Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

def get_dig_sqr_sum(x):
	sum = 0
	for c in str(x):
		sum += int(c)**2
	return sum

etn = 0	
for n in range(1, 10000000):
	x=n
	while x != 1 and x != 89:
		x = get_dig_sqr_sum(x)
		#print(x)
	if x == 89:
		etn += 1
		print(n)
		
		
print(etn)
	