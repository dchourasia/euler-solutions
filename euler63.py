'''
How many n-digit positive integers exist which are also an nth power?

len(x^n) = n

'''
res = []

for x in range(1, 100):
	for p in range(1, 50):
		s = x**p
		#print(s)
		if len(str(s)) == p:
			res.append(s)
			
print(len(set(res)))
			