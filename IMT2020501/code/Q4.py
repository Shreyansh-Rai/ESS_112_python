def is_wellformed(l):
	f=1 #flag that stores 0 if the matrix is not wellformed
	le=len(l[0]) #length of the first row to check equality of other rows with this
	for i in l:
		if(len(i)!=le):
			f=0
			break
	if f==1:
		return True
	else :
		return False

def are_addable(l1,l2):
	if (is_wellformed(l1) and is_wellformed(l2) and len(l1)==len(l2) and len(l1[0])==len(l2[0])):
		return True
	else :
		return False

def are_multipliable(m1,m2):
	if(is_wellformed(m1) and is_wellformed(m2) and len(m1[0])==len(m2)):
		return True
	else :
		return False
def scalar_multiply_list(n,l):
	return[i*n for i in l]

def scalar_multiply_matrix(n,m):
	m1=[] #matrix that will store the scalar multiply matrix 
	for i in m:
		m1.append(scalar_multiply_list(n,i))
	return m1

def add_lists(l1,l2):
	if len(l1)!=len(l2):
		return "lists cannot be added"
	else:
		return [(l1[i]+l2[i]) for i in range(len(l1))]

def add_matrices(m1,m2):
	if are_addable(m1,m2):
		return [add_lists(m1[i],m2[i]) for i in range(len(m1))] 
	else:
		return "matrices cannot be added"
def multiply_lists(l1,l2):
	if len(l1)==len(l2):
		return [l1[i]*l2[i] for i in range(len(l1))]
	else:
		return "Lists cannot be multiplied"

def mattrans(m1):
	p=len(m1) #number of rows in m1
	q=len(m1[0]) #number of columns in m1
	mt=[[0 for j in range(p)] for i in range(q)] #creating a matrix to store the transpose and filling with 0
	for i in range(p):
		for j in range(q):
			mt[j][i]=m1[i][j] #generating the transpose of the matrix
	return mt

def  sum_of_list (l):
	s=0
	for i in l:
		s=s+i
	return s

def multiply_matrices(m1,m2):
	m=[]
	m=[[0 for j in range(len(m2[0]))] for i in range(len(m1))] #initialising the answer matrix
	if(are_multipliable(m1,m2)):
		m2=mattrans(m2) #calculating transpose
		for i in range(len(m1)):
			for j in range(len(m2)):
				m[i][j]= sum_of_list(multiply_lists(m1[i],m2[j])) #multiplying and storing the answer
		return m

	else:
		return "The matrices are not multipliable"

if __name__ == '__main__':
	print(is_wellformed([[1,2,3],[20,40,50]]))
	print(is_wellformed([[1,2,3],[20,40]]))
	print(are_addable([[1,2,3],[20,40,50]],[[1,2,3],[20,40,50]]))
	print(are_addable([[1,2],[20,40]],[[1,2,3],[20,40,50]]))
	print(are_multipliable([[1,2,3],[20,40,50]],[[1,2,3],[20,40,50]]))
	print(are_multipliable([[1,2],[20,40]],[[1,2,3],[20,40,50]]))
	print(scalar_multiply_list(3,[1,2,3]))
	print(scalar_multiply_matrix(2,[[1,2,3],[2,4,5]]))
	print(add_lists([1,2,3],[4,5,6]))
	print(add_matrices([[1,2,3]],[[4,5,6]]))
	print(multiply_lists([1,2,3],[4,5,6]))
	print(multiply_matrices([[1,2,3],[4,5,6]],[[7,10],[8,11],[9,12]]))