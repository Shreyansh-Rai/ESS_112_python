def matmul(m1,m2):
	print(m1)
	print(m2)
	p=len(m1)
	q=len(m2[0])
	c=len(m2)
	if len(m2)!=len(m1[0]) :
		return "The matrices cannot be multiplied"
	res= [[0 for j in range(q)] for i in range(p)]

	for i in range(p) :
		for j in range(q):
			for k in range(c):
				res[i][j]+= m1[i][k]*m2[k][j]
	return res

if __name__=="__main__"	:
	r1=int(input())
	c1=int(input())
	r2=int(input())
	c2=int(input())

rv=matmul([[int(input()) for j in range(c1)] for i in range(r1)],[[int(input()) for j in range(c2)] for i in range(r2)] )
print(rv)


#logic behind matrix mult:
#so what we had to do first was initialise a result matrix that had the same number of rows as m1
#and the same number of columns as m2. the condition for multiplication is that the number of col of m1= rows of m2
#now the loop runs from 0 to p ie number of col of res and inner loop runs from 0 to q ie the number of roes of res
#now in 0,0 in res we needed the sum of products of the corresponding elements of the first row of m1 and the
#first col of m2, for 0,1 we needed the prod of the 1st row of m1 and the second col of m2 and so on
#so we create an innermost loop that goes from 0 to the number of columns of m1 = number of rows of m2
#now we multiply i,k of m1 with k,j if m2 and keep storing and updating the i,j of res. this is how we multiply
#the matrices