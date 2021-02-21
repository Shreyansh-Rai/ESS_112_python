def find_len(lst):
	if(len(lst)==1):
		return 1
	return 1+find_len(lst[1:]) #incrementing the count to be returned
def find_nth_element(n,lst):
	if n==0:
		return lst[0]
	return find_nth_element(n-1,lst[1:]) #keep sending the list until the element to be found is at 0th index
def reverse_list(lst):
	if len(lst)==1:
		return [lst[0]]
	return [lst[len(lst)-1]]+reverse_list(lst[0:len(lst)-1]) #last element+reverse of the list before
if __name__ == '__main__':
	print(find_len([1,2.0,6,9,'xyz']))
	print(find_nth_element(3,[1,2.0,6,9,"CSE","ECE"]))
	print(find_nth_element(0,[1]))
	print(reverse_list([1,2,'a','b']))
