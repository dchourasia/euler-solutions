#pylint:disable=E0001
'''
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''
fracts=[]
def is_cancelling_fraction(x, y):
	if x == y:
		return False
	
	global fracts
	a = set(str(x))
	b = set(str(y))
	is_0_common = '0' in str(x) and '0' in str(y)
	res = False
	
	c = list(a - b)
	d = list(b - a)
	
	
	
	if len(c) == 1 and len(d) == 1 and not is_0_common:
		f = int(c[0])
		g = int(d[0])
		
		if c[0]*2 == str(x) and d[0]*2 == str(y):
			return False
		
		#print(x, y)
		#print(f, g)
		if g > 0 and x/y == f/g and x/y < 1:
			fracts.append((x, y, f, g))
			
	
#x = set(str(49)) - set(str(98))

#print(list(x)[0])
a = [is_cancelling_fraction(x, y) for x in range(10, 99) for y in range(10, 99)]

print(fracts)

print(26/65)

