'''
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

words = open('p042_words.txt').read().split(',')

words = list(map(lambda x: x.replace('"', ''), words))
#print(words[:5])

#print(ord('A')-64)
def get_score(word):
	score = 0
	for c in word.upper():
		score += ord(c) -64
	return score
	
	
#print(max(words, key=lambda x: len(x)))
#print(14*26)

triangles = [int(n*(n+1)/2) for n in range(50)]

tri_words = []

[tri_words.append(w) for w in words if get_score(w) in triangles]

print(len(tri_words))


	