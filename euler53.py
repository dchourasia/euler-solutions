'''
How many, not necessarily distinct, values of 
ncr  for 1 < n < 100 , are greater than one-million?

'''


facts = {}

def get_facts(mx):
	global facts
	f = 1
	facts[0] = 1
	for x in range(1, mx):
		f *= x
		facts[x] = f
		
get_facts(101)

def get_combs(n, r):
	return facts[n]/(facts[r]*facts[n-r])
	
	
ans = [get_combs(n, r) for n in range(23, 101) for r in range(1, n+1) if get_combs(n, r) > 1000000]

print(len(ans))