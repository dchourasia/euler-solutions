'''
Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''
import itertools
def get_pand_nums(x, y):
	s =''
	for n in range(x, y+1):
		s += str(n)
		
	return [''.join(n) for n in itertools.permutations(s)]
	
def fact(n):
	p=1
	while n > 0:
		p *= n
		n -= 1
	return p
	
def is_sub_divisible(n):
	n = str(n)
	if len(n) != 10:
		return False
	x = int(n[1:4])%2 == 0 and int(n[2:5])%3 == 0 and int(n[3:6])%5 == 0 and int(n[4:7])%7 == 0 and int(n[5:8])%11 == 0 and int(n[6:9])%13 == 0 and int(n[7:10])%17 == 0
	return x
#print(len(get_pand_nums(0,9)), fact(10))

sub_div =[]
for x in get_pand_nums(0, 9):
	if is_sub_divisible(x):
		sub_div.append(int(x))
		
		
print(len(sub_div))
print(sum(sub_div))

