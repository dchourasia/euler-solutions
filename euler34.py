
'''
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
'''
def fact_gen():
	n=1
	fact = 1
	while n>0:
		fact *= n
		yield fact
		n += 1
		
f = fact_gen()
facts = {n:next(f) for n in range(1, 10)}

facts[0] = 1
print(facts)

def is_digit_fact(n):
	global facts
	tot = 0
	for x in str(n):
		tot += facts[int(x)]
		
	return  n == tot
	
digit_facts = [x for x in range(3, 1000000) if is_digit_fact(x)]

print(digit_facts)
print(sum(digit_facts))