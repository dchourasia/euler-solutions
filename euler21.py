'''
Evaluate the sum of all the amicable numbers under 10000.
'''
def get_divisor_sum(x):
	
	div = [1]
	if x%2 == 0:
		div.append(2)
		div.append(x//2)
	if x%3 == 0:
		div.append(3)
		div.append(x//3)
		
	n = x//3
	[div.append(i) for i in range(4, n+1) if x%i == 0]
	#print(div)
	return sum(div)

sums = {}
amicables = []
for x in range(1, 1000):
	if x not in sums:
		sums[x] = get_divisor_sum(x)
	if sums[x] not in sums:
		sums[sums[x]] = get_divisor_sum(sums[x])
	if x == sums[sums[x]] and x != sums[x]:
		amicables.append(x)
		amicables.append(sums[x])
		
		
print(amicables)