'''
1! + 4! + 5! = 1 + 24 + 120 = 145
'''

fact = {'0':1}

def get_facts(mx):
	p = 1
	for x in range(1, mx + 1):
		p *= x
		fact[str(x)] = p
		
def dig_fact(x): 
	d = 0
	for c in str(x):
		d += fact[c]
	return d
	
chain_size ={}
	
def get_chain_length(n):
	chain = []
	x = n
	while x not in chain:
		chain.append(x)
		x = dig_fact(x)
	chain_size[n] = len(chain)
	
get_facts(9)

for x in range(10, 1000000):
	get_chain_length(x)
	
print(len([x for x, y in chain_size.items() if y == 60]))

		