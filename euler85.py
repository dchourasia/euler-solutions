'''
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
'''
x, y = 94, 30
def get_rects(x, y):
	s = 0
	for a in range(1, x + 1):
		for b in range(1, y + 1):
			s += a*b
	return s

sums={}
for x in range(20, 50):
	for y in range(50, 100):
		sums[(x, y)] = get_rects(x, y)
print(sorted(sums, key=lambda x: sums[x]))