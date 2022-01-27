'''
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

39 × 186 = 7254
'''
products =[]

def is_pandigital(a, b):
	global products
	p = a*b
	digit = str(a) + str(b) + str(p)
	if len(digit) != 9:
		return False
	s1 = set('123456789')
	if len(s1 - set(digit)) == 0:
		if p not in products:
			products.append(p)
		return True
	
	
pr = [is_pandigital(x, y) for x in range(999) for y in range(9999)]

print(products)

print(sum(products))