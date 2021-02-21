import math

def cross_product(a,b):
	
	def padlist(l1): #pads the list so that they are both having 3 elements
		i=len(l1)
		while(i<3):
			l1.append(0)
			i+=1

		return l1
	

	def dot_product(la,lb): #returns the dot product of the lists
		ldot=[ (la[i]*lb[i]) for i in range(len(la)) ]
		s=0
		for i in ldot:
			s+=i
		return s
	

	def mamgnitude(a): #finds and returns the magnitude of the vectors
		s=0
		for i in a:
			s+=i*i
		return math.sqrt(s)
	
	a=padlist(a)
	b=padlist(b)
	print(a)
	print(b)
	dp=dot_product(a,b)
	ma=mamgnitude(a)
	mb=mamgnitude(b)
	if ma==0 or mb==0 :
		return 0
	cost=dp/(mb*ma)
	if cost==0 or cost<-1 or cost>1: #conditions where the value returned must be 0
		return 0
	sint=math.sqrt(1-cost*cost)
	cp=ma*mb*sint
	return round(cp,2)

if __name__ == '__main__':
	print(cross_product([1,2,3],[4,5,6]))
	print(cross_product([1,2,3],[8,9]))
	print(cross_product([2,3,4],[2,3,4]))
	print(cross_product([0],[2,3,4]))
	print(cross_product([1,-1,0],[-1,1,0]))



