def mattrans(m1):
	p=len(m1) #number of rows in m1
	q=len(m1[0]) #number of columns in m1
	mt=[[0 for j in range(p)] for i in range(q)] #creating a matrix to store the transpose and filling with 0
	for i in range(p):
		for j in range(q):
			mt[j][i]=m1[i][j] #generating the transpose of the matrix
	return mt

if __name__=="__main__":	
	#r=int(input())
	#c=int(input())
	l=mattrans([[1,2],[3,4]])
	print(l)