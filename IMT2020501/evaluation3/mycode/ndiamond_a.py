def ndiamond():                # n is the height of the diamond 
    i=1                         #i,j,k are looping variables
    while (i<=3):
      j=2
      while(j > i-1):
        print "\b" + " ",               #'\b' is a backspace escape character used to remove the terminating space
        j-=1
      k=1
      while(k<=i):
        print "\b" + str(k),
        k+=1
      if(i >= 2):
        m = i -1
        while(m>0):
          print "\b" + str(m),
          m-=1
      print""
      i+=1
    i = 2
    while(i > 0):
      j = 0
      while (j < 3-i):
        print"\b" + " ",
        j+=1
      k=1
      while(k < i+1):
        print"\b" + str(k),
        k+=1
      m = i -1
      while(m>0):
        print"\b" + str(m),
        m-=1
      print""
      i-=1

  
