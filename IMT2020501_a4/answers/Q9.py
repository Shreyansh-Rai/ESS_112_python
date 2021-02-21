def even_elements(l):
	return [i for i in l if i%2==0]

if __name__ == '__main__':
	print(even_elements([0,1,2,3,4,5,6,7,8,9]))