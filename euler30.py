'''
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import math

nums = []
for n in range(10, 200000):
	sumt=0
	for d in str(n):
		sumt += math.pow(int(d), 5)
	if int(sumt) == n:
		nums.append(n)
		
print(nums)
print(sum(nums))