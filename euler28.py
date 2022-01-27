'''
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''


# 5	17	37
# 1 + sqr(2n) 	for n = 1 to 500

#1	9	25
# sqr(2n - 1) 	for n = 1 to 501

import math
s1 = [1 + math.pow(2*n, 2) for n in range(1, 501)]

s2 = [math.pow(2*n - 1, 2) for n in range(1, 502)]

#print(sum(s1 + s2))

#print(s2)


#1	7	21	43
# sqr(2n - 1) - (2n - 1)  + 1
#4n2 - 4n + 1 - 2n +2
#4n2- 6n + 3		for n = 1 to 501

#3	13	31
#sqr(2n - 1) + 2n
#4n2 - 2n + 1		for n = 1 to 500

s3 = [4*n*n - 6*n + 3 for n in range(1, 502)]

s4 = [4*n*n - 2*n + 1 for n in range(1, 501)]

print(sum(s1 + s2 + s3 + s4) - 1)
# -1 because central 1 is counted in 2 lists



