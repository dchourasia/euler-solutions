'''
What is the sum of the digits of the number 2^1000?

'''


p = pow(2, 1000)

print(sum([int(x) for x in str(p)]))
