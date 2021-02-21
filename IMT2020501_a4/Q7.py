def double(l):
	ltpd=[]
	ltp=[]
	for i in l:
		ltpd.append(int(i)*2)
		ltp.append(int(i))
	return ltpd,ltp
ltp= input().split(',')
ltgd,ltg= double(ltp)
print("input =",ltg)
print(ltgd)