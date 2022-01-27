'''
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import itertools
def get_divisor_sum(x):
	div = [1]
	opt  = 100 if x > 100 else 1
	for i in range(2, opt+1):
		if x%i == 0:
			div.append(i)
			div.append(x//i)
	n = x//opt
	[div.append(i) for i in range(opt+1, n) if x%i == 0]
	#print(div)
	return sum(div)
	
def is_perfect_number(n):
	return n == get_divisor_sum(n)

def is_abundant_number(n):
	return get_divisor_sum(n) > n
	
abundant_nums = []

for x in range(1, 28123):
	
	if is_abundant_number(x):
		abundant_nums.append(x)
		
sums = set([sum(x) for x in itertools.product(abundant_nums, abundant_nums) if sum(x) < 28124])
#print(abundant_nums)
print(list(sums)[:100])
total = 0
all = set(range(1, 28124))
print(len(all))
print(sum(all - sums))


		
print(total)
