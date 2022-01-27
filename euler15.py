#pylint:disable=E0001
'''
How many such routes are there through a 20×20 grid?

'''
total = 0

def get_routes(x, y, currentX=0, currentY=0):
	global total
	
	if currentX < x and currentY < y:
		if (currentX, currentY) == (0, 0):
			total += 2
		else:
			total += 1
		get_routes(x, y, currentX+1, currentY)
		get_routes(x, y, currentX, currentY+1)
	#else:
	#	total += 1
		
	#if currentY < y:
	#	total += 1
	#	get_routes(x, y, currentX, currentY+1)
	#else:
	#	total += 1
	
def get_two_power_sums(n):
	res = 0
	for i in range(0, n):
		res += pow(2, i)
		
	return res*2
def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)
		
def all_routes(n):
	return fact(2*n)/pow(fact(n), 2)
	
#get_routes(3, 3)
#print(total)
#print(get_two_power_sums(20))

print(all_routes(20))