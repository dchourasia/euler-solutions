'''
x^2 – Dy^2 = 1

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

'''
import math
res ={}
nf = []
for D in range(2, 1000):
	if not math.sqrt(D).is_integer():
		found = False
		for x in range(1150000, 1160000):
			y = math.sqrt(((x*x - 1)/D))
			if y.is_integer():
				#print(x, y, D)
				res[D] = x
				found = True
				break
		if not found:
			nf.append(D)

#print(nf, len(nf))
print(res, len(res))
print(max(res, key=res.get))
			
			