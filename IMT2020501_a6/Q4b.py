def flatten(lst):
	ltbp=[]
	for i in lst:
		if isinstance(i,list): #if it is a list then iterate through it and append 
			for j in i:
				ltbp.append(j)
		else: #if single elements then directly append
			ltbp.append(i)
	if len(lst)==1 : #if the list has only one element then return as is
		return lst
	return flatten((ltbp[0:1]))+flatten((ltbp[1:])) #recursive call. 

if __name__ == '__main__':
	print(flatten([[8, 9], [10, 11, 'iiitb'], [13]]))
	print(flatten([['A', 'B', 'C'], ['D','E', 'F']]))