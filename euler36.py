'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
'''

def get_binary(n):
	bin=''
	while n> 0:
		bin += str(n%2)
		n = n//2
		
	#print(bin[::-1])
	return bin[::-1]
	
def is_palindrom(n):
	return str(n) == str(n)[::-1]
	
double_pals =[]


for n in range(1000000):
	if is_palindrom(n) and is_palindrom(get_binary(n)):
		double_pals.append(n)
	
print(sum(double_pals))
	
