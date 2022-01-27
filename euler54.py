'''
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.


How many hands does Player 1 win?
'''
values = {}
for x in range(2, 10):
	values[str(x)] = x
values['T'] = 10
values['J'] = 11
values['K'] = 12
values['Q'] = 13
values['A'] = 14


data = open('p054_poker.txt').readlines()
print(len(data))

def get_cards(line):
	res = [[], []]
	for i, x in enumerate(line.strip().split(' ')):
		y = 0 if i < 5 else 1
		res[y].append((values[x[0]], x[1]))
	return res
	
def get_winner(cards):
	c1 = sorted(cards[0], key=lambda x: x[0])
	c2 = sorted(cards[1], key=lambda x: x[0])
	print(c1, c2)
	winner = 0
	tie = False
	winner = eval_winner(c1, c2)
	return winner
	
	

def is_1_pair(c):
	vals = [x[0] for x in c]
	cts = set([vals.count(x) for x in set(vals)])
	cts_dict = {x:vals.count(x) for x in set(vals)}
	h = sorted([x for x, y in cts_dict.items() if y == 2])
	
	return 2 in cts, h
	
def get_rank(c):
	defs = [is_royal_flush, is_straight_flush, is_4_of_a_kind, is_full_house, is_flush, is_straight, is_3_of_a_kind, is_2_pairs, is_1_pair]
	rank=100
	for i, func in enumerate(defs):
		r, h = func(c)
		if r:
			print('setting rank', i, func.__name__)
			if i < 4:
				raise Exception('lower ranks found')
			rank=i
			break
	return rank, h
			
	
def is_2_pairs(c):
	vals = [x[0] for x in c]
	cts = [vals.count(x) for x in set(vals)]
	cts_dict = {x:vals.count(x) for x in set(vals)}
	h = sorted([x for x, y in cts_dict.items() if y == 2])
	print('cts', cts)
	print('vals', vals)
	return [1, 2, 2] == sorted(cts), h
	
def is_3_of_a_kind(c):
	vals = [x[0] for x in c]
	cts = set([vals.count(x) for x in set(vals)])
	cts_dict = {x:vals.count(x) for x in set(vals)}
	h = sorted([x for x, y in cts_dict.items() if y == 3])
	return 3 in cts, h
	
def is_straight(c):
	init = c[0][0]
	for i, card in enumerate(c[1:]):
		if card[0] != init + i + 1:
			return False, c[4][0]
	return True, c[4][0]
	
def is_flush(c):
	suits = set([x[1] for x in c])
	return len(suits) == 1, [c[4][0]]
	
def is_full_house(c):
	vals = [x[0] for x in c]
	cts = [vals.count(x) for x in set(vals)]
	cts_dict = {x:vals.count(x) for x in set(vals)}
	h1 = [x for x, y in cts_dict.items() if y == 3]
	h2 = [x for x, y in cts_dict.items() if y == 2]
	return [2, 3] == sorted(cts) in cts, h1 + h2
	
	
def get_winner_on_highest_card(c1, c2):
	print('deciding on higher card')
	c1 = sorted(c1, key=lambda x: x[0], reverse=True)
	c2 = sorted(c2, key=lambda x: x[0], reverse=True)
	winner = 0
	for x, y in zip(c1, c2):
		print(x[0], y[0])
		if x[0] != y[0]:
			winner = int(y[0] > x[0]) + 1
			break
	return winner
				
def eval_winner( c1, c2):
	tie=False
	winner = 0
	if not winner:
		r1, h1 = get_rank(c1)
		r2, h2 = get_rank(c2)
		print(r1, h1)
		print(r2, h2)
		if r1 == r2 and r1 != -1:
			print('rank tie', r1)
			for x, y in zip(h1, h2):
				if x != y:
					winner = int(y > x) + 1
					break
			if not winner:
				tie=True
		elif r1 == r2 == -1:
			print('no rank tie')
			tie=True
		else:
			winner = int(r2 < r1) + 1
		
	if tie:
		winner = get_winner_on_highest_card(c1, c2)	
	return winner

def is_4_of_a_kind(c):
	vals = [x[0] for x in c]
	cts = set([vals.count(x) for x in set(vals)])
	cts_dict = {x:vals.count(x) for x in set(vals)}
	h = sorted([x for x, y in cts_dict.items() if y == 4])
	return 4 in cts, h
	
def is_straight_flush(c):
	s=c[0][1]
	for card in c:
		if card[1] != s:
			return False, [c[4][0]]
	init = c[0][0]
	for i, card in enumerate(c[1:]):
		if card[0] != init + i + 1:
			return False, [c[4][0]]
			
	return True, [c[4][0]]
	
def is_royal_flush(c):
	s=c[0][1]
	for card in c:
		if card[1] != s:
			return False, [c[4][0]]
	for i, card in enumerate(c):
		if card[0] != i + 10:
			return False, [c[4][0]]
			
	return True, [c[4][0]]
			
winners = []
for line in data:
		winner = get_winner(get_cards(line))
		print(winner)
		winners.append(winner)
		
#print(int(False))

print(winners.count(1))

a = [2, 2, 3, 1]
b = [2, 1, 2]
#x = a.sort()
#print(2 in set(a))
#print(a+b)
#print(all(x in a for x in b))


		
