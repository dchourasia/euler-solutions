'''
What is the value of the first triangle number to have over five hundred divisors?
'''

chunk = 100

def get_triangle_number(n):
	return int(n*(n+1)/2)
	
	
def get_divisor_count(x):
	div = [1]
	opt  = 100
	for i in range(2, opt+1):
		if x%i == 0:
			div.append(i)
			div.append(x//i)
	n = x//opt
	[div.append(i) for i in range(opt+1, n+1) if x%i == 0]
	#print(div)
	return len(div)
	
mx = 0
for i in range(123, 124):
	for x in [get_triangle_number(n) for n in range(100*i, 100*(i+1))]:
		t = get_divisor_count(x)
		mx = max(t, mx)
		if mx >= 500:
			print(x)
			break
	
	print(mx)
	mx = 0
	
	

	
	