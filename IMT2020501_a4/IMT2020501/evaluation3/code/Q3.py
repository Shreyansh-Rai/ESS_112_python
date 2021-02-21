def banner(m): #gets a message m
	l=len(m) 
	print("*"*(l+4)) #upper banner row
	print("*",m,"*") #middle row
	print("*"*(l+4)) #lower row

if __name__=="__main__" :
	banner("Good Morning!")
