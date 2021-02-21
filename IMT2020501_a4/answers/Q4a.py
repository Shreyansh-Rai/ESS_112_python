def diamond():
	for i in range(3): #printing the upper triangle of rows
		for j in range(2-i):        #each row has 2-i spaces before the *
			print(" ",end="")
		for j in range(2*i+1):      #row 1 has 1 * row 2 has 3 stars so 2n+1 *
			print("*",end="")
		print()
	for i in range(2): #printing the lower rows
		for j in range(i+1):        #printing the spaces which 1 for the first row then 1+1  => i+1 " "     
			print(" ",end="")       
		for j in range(3-2*i):      # first row has 3 stars then 1 so 3-2n
			print("*",end="")
		print()


if __name__=="__main__":
	diamond() #printing the first 3 rows