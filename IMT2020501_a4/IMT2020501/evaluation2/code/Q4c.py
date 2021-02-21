def diamond(n,c):
	u=int(n/2)+1   #number of rows in the upper triangle
	l=int(n/2)     #number of rows in the lower tirangle
	for i in range(u):  #for the upper triangle
		for j in range(u-1-i):  #printing spaces 
			print(" ",end="")
		for j in range(2*i+1):  #printing the * 
			print(c,end="")
		print()
	for i in range(l):          #for the lower triangle
		for j in range(i+1):    #printing the spaces in the lower triangle
			print(" ",end="")
		for j in range(n-2*(i+1)):   #printing the *s in the lower triangle
			print(c,end="")
		print() 

if __name__=="__main__":
	diamond(int(input()),input())  