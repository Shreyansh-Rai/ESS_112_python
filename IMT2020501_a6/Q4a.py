def total_sum(lst):
	ltbp=[]
	for i in lst:
		if isinstance(i,list): #if list iterate and append elements
			for j in i:
				ltbp.append(j)
		else: #directly append if single element
			ltbp.append(i)
	if len(lst)==1 and (isinstance(lst[0],int) or isinstance(lst[0],float)):
		return lst[0] #return the element to be added
	elif len(lst)==1: #if the length of the list is 1 and the element is not addable then return 0
		return 0
	return total_sum((ltbp[0:1]))+total_sum((ltbp[1:]))

if __name__ == '__main__':
	print(total_sum([[1, 2.5, 3],[4,['abc',6],7]]))
	print(total_sum([1, 2.2, [3]]))