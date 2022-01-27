'''
Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
'''
fib = [1, 1]
def get_next_fib(mx):
	n=1
	last, curr = 0, 1
	global fib
	while n <= mx:
			last, curr = curr, last + curr
			n += 1
			yield n , curr
			
	
def get_fib_series(mx):
	while len(fib) < mx:
		fib.append(fib[-1] + fib[-2])


def is_pand(x):
	a = '214365879'
	x = str(x)
	return len(x) == len(set(x)) and set(x) == set(a)
	
#x = [n for n in get_next_fib(10)]
#print(x)
x = 123456789

#print(is_pand(x))

for i, x in get_next_fib(275500):
	if i >= 27550:
		pand = is_pand(str(x)[:9]) and is_pand(str(x)[-9:])
		if pand:
			print(i)
			break
		#print(str(x)[:9], str(x)[-9:])
		




	