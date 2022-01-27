'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
n = 100

sqos = pow(sum([x for x in range(1, n+1)]), 2)
sosq = sum([x*x for x in range(1, n+1)])

print(sqos-sosq)