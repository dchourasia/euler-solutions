'''
Find the sum of the digits in the number 100!
'''

def fact(n):
	return 1 if n <= 1 else n*fact(n-1)
	
print(sum(map(int, [x for x in str(fact(100))])))