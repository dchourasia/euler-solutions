'''
non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.
'''
n = 3
arr = []
for x in range(1, 50):
	p = str(2**x)
	n_dig = p[-3:]
	if len(n_dig) == n:
		if arr and arr[0] == n_dig:
			repeat = True
		else:
			arr.append(n_dig)
	if 
	print(x, n_dig)
	

#print(str(28433*2**100 + 1)[-10:])

#print(str(2**57))
#print(str(2**10157))



