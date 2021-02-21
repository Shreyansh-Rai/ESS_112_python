def diamond(n):      # n is the height of the diamond 
    i=1             #i,j,k are looping variables
    l = (n+1)/2     # l is the height of the top half pyramid of the diamond
    while (i<=l):
        j=l -1
        while(j > i-1):         
            print "\b" + " ",   #'\b' is a backspace escape character used to remove the terminating space
            j-=1
        k=1
        while(k < 2*i):
            print "\b" + "*",
            k+=1
        print""
        i+=1
    i = l - 1
    while(i > 0):
        j = 0
        while (j < l-i):
            print"\b" + " ",
            j+=1
        k =0
        while(k < (i*2)-1):
            print "\b" + "*",
            k+=1
        print""
        i-=1




