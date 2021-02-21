def ndiamond(n):
	u=int(n/2)+1  #number of rows in the upper triangle
	l=int(n/2)    #number of rows in the lower tirangle
	k=1
	for i in range(u):   #for the upper triangle
		k=1
		for j in range(u-1-i):   #printing spaces 
			print(" ",end="")
		for j in range(2*i+1):   #for printing the numbers 2n-1 times for the nth row n>=0
			print(k,end="")      #now we print k which starts from 1 k increases untill i==j then it decreases
			if j<i :
				k+=1
			else:
				k-=1
		print()
	for i in range(l):           #for the lower triangle 
		k=1
		for j in range(i+1):     #printing spaces
			print(" ",end="")
		for j in range(n-2*(i+1)):  # print the numbers n-2(i+1) times 
			print(k,end="")         #again we print k starting from one and we increment it till k is 
			if j<l-i-1 :            #less than l-1-i then it is decremented
				k+=1
			else:
				k-=1

		print()

if __name__=="__main__" :
	ndiamond(int(input()))