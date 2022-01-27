'''
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def is_pand(n):
	return '0' not in str(n) and len(str(n)) == 9 and len(set(str(n)) ) == 9
	
m = 100000
pands = {}
for n in range(1, m):
	p = ''
	for x in range(1, 10):
		p += str(n*x)
		if len(set(p)) < len(p):
			break
		elif is_pand(p):
			pands[(n, x)] = int(p)
			break
			
			
print(max(pands), pands[max(pands)])
			
	
	
