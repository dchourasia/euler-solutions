'''
2xy = l^2 - 2lz
2xy = 2lx + 2ly - l^2
Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
1 + cos@ + sin@ = l/z
'''
single_sides = []

def get_sides(p):
	global single_sides
	#hf = int(p/2)
	
	hf = int(p/(2 + 1/(2**0.5)))
	#print(hf)
	#sides = [(x, y, p - x - y) for x in range(1, hf) for y in range(1, x) if 2*p*x + 2*p*y - p*p - 2*x*y == 0]
	sides = []
	for x in range(1, hf):
		'''
		for y in range(1, x):
			if 2*p*x + 2*p*y - p*p - 2*x*y == 0:
				sides.append((x, y, p - x - y))
			if len(sides) > 1:
				break
		'''
		y = (p*p - 2*p*x)/(2*p - 2*x)
		if y.is_integer():
			lst = list(map(lambda n: str(int(n)), [x, y, p - x - y]))
			entry = '+'.join(sorted(lst))
			if entry not in sides:
				sides.append(entry)
				#print(x, y, p - x - y)
		
		if len(sides) > 1:
			break
	if len(sides) == 1:
		single_sides.append(p)
		#print(sides)
	return sides
	
def process_list(rng):
	#print(rng)
	for x in rng:
		get_sides(x)
		#print(x)
	print(rng, 'done')

process_list(range(0, 10000))

'''
from multiprocessing.pool import ThreadPool
s, e, pools = 0, 10000, 5
chunk = int((e - s)/pools)
pool = ThreadPool(pools)
ranges = [range(s + x*chunk, s + (x+1)*chunk) for x in range(0, pools)]

result = pool.map_async(process_list, ranges)
result.wait()
print(result.__dict__)
pool.close()
'''
print(len(single_sides))
