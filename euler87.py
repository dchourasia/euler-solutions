'''
How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''



import math
primes=[]
sqr, cube, quad = [], [], []
def get_primes(mx):
	x=1
	global sqr, cube, quad
	mx_sqr = int(mx**(1/2))
	mx_cube = int(mx**(1/3))
	mx_quad = int(mx**(1/4))
	while x < mx_sqr:
		x+=1
		y=int(math.sqrt(x))
		isprime=True
		for z in primes:
			if z > y:
				break
			if x%z==0:
				isprime=False
				break
		if isprime:
			primes.append(x)
			sqr.append(x)
			if x < mx_cube:
				cube.append(x)
			if x < mx_quad:
				quad.append(x)
			
			
mx = 50000000
fix_mx = 50000000	
req = int(mx**(1/2))	
print(req*req)
get_primes(mx)
mpr = primes[-1]
print(mpr**2)


#print(len(primes)**3)
print(sqr[-1]**2, cube[-1]**3, quad[-1]**4)
print(cube, quad)
print(len(sqr), len(cube), len(quad))
nums = [x**2 + y**3 + z**4 for x in sqr for y in cube for z in quad if x**2 + y**3 + z**4 <= fix_mx ]
print(len(set(nums)))