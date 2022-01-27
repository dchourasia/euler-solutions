'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

#sqr(p) - 2p(x + y) +2xy = 0

#all the sides will be less than p//2
solutions={}
def get_solutions(p):
	global solutions
	l=p//2
	sols = [(x,y) for x in range(1, l//2+1) for y in range(l//2, l) if p*p - 2*p*(x+y) + 2*x*y == 0]
	
	#print(sols)
	solutions[p] = sols
	
for x in range(2, 1001):
	get_solutions(x)
	
mx = max(solutions, key=lambda x: len(solutions[x]))

print(mx, solutions[mx])

	
	

