'''
Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
'''

data = open('p059_cipher.txt').read().split(',')
dec = []
import re
all = 'abcdefgijklmnopqrstuvwxyz'
import itertools
keys = itertools.permutations(all, 3)
finalKey = ''
for key in keys:
	s = ''
	for i, c in enumerate(data[:50]):
		s += chr(int(c)^ord(key[i%3]))
	m = re.match('^[a-zA-Z ]{50}$', s)
	if m:
		print(key)
		finalKey = key
		break
		#dec.append(s)

s = ''
sm = 0
for i, c in enumerate(data):
	d = chr(int(c)^ord(finalKey[i%3]))
	s += d
	sm += ord(d)
print(s, sm)

#[print(s) for s in dec]
#print(s)
#print(65^42)
