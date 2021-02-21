def transpose(m1):
	print(m1)
	p=len(m1)
	q=len(m1[0])
	mt=[[0 for j in range(p)] for i in range(q)]
	for i in range(p):
		for j in range(q):
			mt[j][i]=m1[i][j]
	return mt

r=int(input())
c=int(input())
l=transpose([[int(input()) for j in range(c)] for i in range(r)])
print(l)