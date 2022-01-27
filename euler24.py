'''
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from itertools import permutations

perm = permutations(list(range(0, 10)))

print(list(perm)[1000000-1])