#n>1 p>=0 and we must recursively find out n^p
def power(n,p):
	if p==0:
		return 1
	return n*power(n,p-1) #simple recursion for multiplying the value n p times

if __name__ == '__main__':
	print(power(2,3))
	print(power(1,0))
	print(power(2,0))
	print(power(3,3))