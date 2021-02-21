'''def even_elements(l):
	ltpd=[]
	ltp=[]
	for i in l:
		if int(i)%2==0:
			ltpd.append(int(i))
		ltp.append(int(i))
	return ltpd,ltp
ltp= input().split(',')
ltgd,ltg= even_elements(ltp)
print("input =",ltg)
print(ltgd)'''
def even_elements(l):
	return [i for i in l if i%2==0]

if __name__ == '__main__':
	print(even_elements([0,1,2,3,4,5,6,7,8,9]))