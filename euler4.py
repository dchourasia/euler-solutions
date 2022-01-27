'''
Find the largest palindrome made from the product of two 3-digit numbers.

'''
import itertools
def ispalindrome(n):
	return str(n) == str(n)[::-1]
	
nums = [x for x in reversed(range(100, 1000))]
prod = 0
palindromes ={}
for x, y in itertools.product(nums,nums):
	prod = x*y
	if ispalindrome(prod):
		#print(x, y)
		palindromes[prod] = (x, y)
		
maxp = 	max(palindromes.keys())
print(maxp, palindromes[maxp])


