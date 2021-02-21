def increment (n):
	return (n+1)

def decrement (n):
	return(n-1)

def add(a,b):
	for i in range(b):
		a= increment(a)
	return a

def subtract(a,b):
	for i in range(b):
		a=decrement(a)
	return a

def multiply(a,b):
	s=0
	for i in range(b):
		s=add(s,a)
	return s

def divide(a,b):
	k=0 #stores the quotient
	while(a):
		a=subtract(a,b)
		k=increment(k)
	return k

def exponent(a,b):
	s=1
	for i in range(b):
		s=multiply(s,a)
	return s



if __name__ == '__main__':
	print(increment(-2))
	print(decrement(1))
	print(add(1,2))
	print(subtract(1,2))
	print(multiply(2,3))
	print(divide(6,3))
	print(exponent(3,2))