def diamond(n,c):
	u=int(n/2)+1
	l=int(n/2)
	for i in range(u):
		for j in range(u-1-i):
			print(" ",end="")
		for j in range(2*i+1):
			print(c,end="")
		print()
	for i in range(l):
		for j in range(i+1):
			print(" ",end="")
		for j in range(n-2*(i+1)):
			print(c,end="")
		print()
diamond(int(input()),input())