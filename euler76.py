'''
How many different ways can one hundred be written as a sum of at least two positive integers?.
5
0 <= x <= 5
'''
all_combs = []
c=0
def find_combs(comb, n, dig):
	global c
	if dig >= n:
		return 
	curr_total = sum(comb[:dig])
	#if curr_total > n:
		#	return 
	total = sum(comb)
	if total == n:
			#print(comb)
			all_combs.append(''.join(map(str, sorted(comb))))
			#return 
	for x in range(dig, n):
			comb[dig] = x
			print(n, dig, comb)
			c += 1
			find_combs(comb, n, dig+1)

n = 5
find_combs([0]*n, n, 0)
print(c)
#print(set(all_combs))
		
