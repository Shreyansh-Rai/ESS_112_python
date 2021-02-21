def product_of_list(l):
	s=1 #stores the product
	for i in l:
		s=s*i 
	return(s)

def reduce_terms(l1):
	lr=[]
	for i in l1 :
		lr.append(product_of_list(i))
	return lr
def  sum_of_list (l):
	s=0
	for i in l:
		s=s+i
	return s

def evaluate_SOP(l):
	return(sum_of_list(reduce_terms(l)))



if __name__ == '__main__':
	print(product_of_list([1,2,3])) 
	print(reduce_terms([[1,2,3],[20,40],[1]]))
	print(sum_of_list([6,800]))
	print(evaluate_SOP([[1,2,3],[20,40],[1]]))