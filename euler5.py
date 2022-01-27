n = 20

res = 1
for i in range(2, n+1):
	if res%i != 0:
		for j in range(2, i+1):
			if (j*res)%i == 0:
				res = j*res
				print(j)
				break
print(res)