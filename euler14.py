'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?
'''

def get_collatz_seq_length(n):
	count = 1
	while n != 1:
		n = int(n/2) if n%2 == 0 else 3*n + 1
		count += 1
		
	return count
	
	
lens={}
for x in range(2, 1000000):
	lens[x] = get_collatz_seq_length(x)
	
	
mx = max(lens, key=lambda x: lens[x])

print(mx, lens[mx])
	
	
	
	

		
	