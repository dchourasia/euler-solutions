'''
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
dec = 0.07692307692307693

def find_pattern(x):
	s = str(x).replace('0.', '')
	pat = ''
	started = False
	start_idx=0
	repeat=''
	cycle=1
	for i, c in enumerate(s[:-1]):
		#print(c, pat)
		if pat and c == pat[0] and not started:
			started=True
			start_idx=i
			repeat+=c
		elif started:
			#print(i-cycle*len(pat) , len(pat) - 1)
			if i-cycle*len(pat) <= len(pat) - 1:
				if pat[i-cycle*len(pat)] == c:
					repeat+=c
					if i-cycle*len(pat) == len(pat) - 1 and repeat==pat:
						repeat=''
						started=False
						start_idx=0
						cycle+=1
				else:
					repeat+=c
					started=False
					start_idx=0
					pat+=repeat
					repeat=''
					#print('else1')
					
			else:
				repeat+=c
				started=False
				start_idx=0
				pat+=repeat
				repeat=''
				#print('else2')
		else:
			pat += c
				
	#print(pat, len(pat))
	return pat

x = str(format(1/10, '.100f'))
#find_pattern(x)

#print(len(x))
#print(x)
lens =[]
for i in range(3, 4):
	x = str(format(1/i, '.100f'))
	print(i, x)
	pat = find_pattern(x)
	


