'''
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
for x in range(100000, 200000):
	if set(str(2*x)) == set(str(3*x)):
		if set(str(3*x)) == set(str(4*x)):
			if set(str(4*x)) == set(str(5*x)):
				if set(str(5*x)) == set(str(6*x)):
					print(x)
		