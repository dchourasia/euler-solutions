'''
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
def get_fibonacci_num():
	series = [1, 1]
	n = 0
	
	
	while n >= 0:
		x = None
		if n < 2:
			x = series[n]
		else:
			x = series[n-1] + series[n-2]
			series.append(x)
		yield x
		n += 1

for i, v in enumerate(get_fibonacci_num()):
	if len(str(v)) == 1000:
		print(i+1)
		break