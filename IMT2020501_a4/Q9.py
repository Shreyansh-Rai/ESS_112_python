def balanced_brackets():
	li=input().split(",")
	lo=[]
	lc=[]
	for i in li:
		if i=='(' or i=='{' or i=='[' :
			lo.append(i)
		else :
			lc.append(i)
	k=len(lo)-1
	i=0
	if k!=len(lc)-1 :
		return False
	while True :
		if k<0:
			return True
		if lo[k]=='(' and lc[i]==')' or lo[k]=='{' and lc[i]=='}' or lo[k]=='[' and lc[i]==']':
			k-=1
			i+=1
		else :
			return False

bo=balanced_brackets()
print(bo)

