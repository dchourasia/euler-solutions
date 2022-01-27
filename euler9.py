'''
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
'''
def multi(tup):
	prod=1
	for n in tup:
		prod*= n
	return prod
result =[]
pairs = [result.append((a, b, c)) for a in range(0, 1000) for b in range(0, 500) for c in range(0, 500) if a+b+c==1000 and a*a + b*b == c*c and not len(result)]
print(result)
if len(result):
	print(multi(result[0]))
	
