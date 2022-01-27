'''
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

How many different ways can £2 be made using any number of coins?

$2 == 1
$1*2 == 1
'''




combs = [(a, b, c, d, e, f, g) for a in range(0, 200) for b in range(0, 100) for c in range(0, 40) for d in range(0, 20) for e in range(0, 10) for f in range(0, 4) for g in range(0, 2)  if a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 == 200]

print(combs)

print(len(combs))