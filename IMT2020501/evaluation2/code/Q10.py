def balanced_brackets(s):
	stack=[] 
	lo=['(','{','[']	#list of open brackets
	lc=[')','}',']']	#list of closed brackets
	for i in s:
		if i in lo:	#if the character is found in the list of open brackets add to stack
			stack.append(i) 
		elif i in lc: #if bracket is closing then the last opened bracket must close first
			if len(stack)>0 and stack[len(stack)-1] == lo[lc.index(i)] : #if stack not empty check for bracket equality
				stack.pop() #pop brackets for which we have checked closing brackets exist
			else : #either length of the stack is 0 or it is not 0 and brackets do not match
				return False
	if stack :   #if after checking all the brackets the stack is not empty then the brackets are
		return False #unbalanced
	else :
		return True
if __name__=="__main__" :
	print( balanced_brackets ( "[](" ))
	print( balanced_brackets ( "}{()" ))