def diamond():
	n=5
	u=int(n/2)+1
	l=int(n/2)
	k=1
	for i in range(u):
		k=1
		for j in range(u-1-i):
			print(" ",end="")
		for j in range(2*i+1):
			print(k,end="")
			if j<i :
				k+=1
			else:
				k-=1
		print()
	for i in range(l):
		k=1
		for j in range(i+1):
			print(" ",end="")
		for j in range(n-2*(i+1)):
			print(k,end="")
			if j<l-i-1 :
				k+=1
			else:
				k-=1

		print()

if __name__=='__main__':
	diamond()