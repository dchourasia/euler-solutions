'''
p3 = n(n+1)/2
p4 = sqr(n)
p5 = n(3n - 1)/2
p6 = n(2n-1)
p7 = n(5n-3)/2
p8 = n(3n-2)

4 digit cyclic numbers for n=3, 4, 5
'''

x, y, z = 'ab', 'bc', 'ca'

p3, p4, p5, p6, p7, p8 = [], [], [], [], [], []
for n in range(30, 150):
	p3.append(int(n*(n+1)/2))
	p4.append(n*n)
	p5.append(int(n*(3*n-1)/2))
	p6.append(n*(2*n-1))
	p7.append(int(n*(5*n-3)/2))
	p8.append(n*(3*n-2))
	
p3 = [x for x in p3 if len(str(x)) == 4]
p4 = [x for x in p4 if len(str(x)) == 4]
p5 = [x for x in p5 if len(str(x)) == 4]
p6 = [x for x in p6 if len(str(x)) == 4]
p7 = [x for x in p7 if len(str(x)) == 4]
p8 = [x for x in p8 if len(str(x)) == 4]

print(p3[:5], p3[:-5:-1])
print(p4[:5], p4[:-5:-1])
print(p5[:5], p5[:-5:-1])
print(len(p3), len(p4), len(p5), len(p6), len(p7), len(p8))
#print(8128 in p3, 2882 in p5, 8281 in p5)

def is_cyclic(lst):
	uniq = []
	s = len(lst)
	lst = [str(x) for x in lst]
	firsts = []
	lasts = []
	for x in lst:
		tmp = [x[0:2], x[2:]]
		if len(set(tmp)) != 2:
			return False
		uniq += tmp
		firsts.append(tmp[0])
		lasts.append(tmp[1])
		
	return len(set(firsts)) == s and len(set(lasts)) == s  and len(set(uniq)) == s
	
found = False
for a in p3:
	for b in p4:
		for c in p5:
			for d in p6:
				for e in p7:
					for f in p8:
						if is_cyclic([a, b, c, d, e, f]):
							print(a, b, c, d, e, f)
							found= True
							break
					if found:
						break
				if found:
					break
			if found:
				break
		if found:
			break
	if found:
			break
			



