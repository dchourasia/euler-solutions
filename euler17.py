'''
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ","twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "] 
 
twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "] 


#assuming it only for 3 letter digits
def get_pronunciation(n):
	if len(str(n))> 3:
		raise Exception('4 digit numbers not supported')
		
	res =''
		
	if n < 20:
		return ones[n]
	elif len(str(n)) == 2:
		unit = n%10
		decade = n//10
		return twenties[decade] + ones[unit]
		print(unit, decade)
	elif len(str(n)) == 3:
		unit = n%10
		decade = (n//10)%10
		ternary = n//100
		last_two = n%100
		if last_two == 0:
			return ones[ternary] + 'hundred'
		elif last_two < 20:
			return ones[ternary]+ 'hundred and ' + ones[last_two]
		else:
			return ones[ternary]+ 'hundred and ' + twenties[decade] + ones[unit]
		print(unit, decade, ternary)


words = ''
for n in range(1, 1000):
	word = get_pronunciation(n)
	#print(word)
	words += word
	
words += 'one thousand'


words = words.replace(' ', '')
print(len(words))
#print(words)
#print(372%100)