from math import factorial
def pascal_triangle(n):

	if n==1:  #if n is one prints one as it is supposed to be the only element in the first row and then returns control
		print(1)
		return
	pascal_triangle(n-1)#recursive call for n-1
	def ncr(n,r): #calculates the factorial
		return int(factorial(n)/(factorial(r)*factorial(n-r)))
	for i in range(n):
		if i==(n-1): #no space after the last element has been printed in the row
			print(ncr(n-1,i),end="")
		else:
			print(ncr(n-1,i),end=" ") #calculating and printing the ncr for each element 
	print()
if __name__ == '__main__':
	pascal_triangle(5)
	pascal_triangle(7)
    