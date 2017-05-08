
#new=inlist.split(",")
#print(new)
#print len(inlist)

inp=int(raw_input("What problem do you want to solve? \n 1.Flattening the list \n 2.Counting the occurences of each element in a string\n"))

if inp ==1:
	def flatten_list(inlist):
		for i in inlist:
			if type(i)==list:
				flatten_list(i)
			else:
				outlist.append(i)
		return(outlist)

	nested_list=[1,2,[3,4,[5,6,7],8],9]

	print "The nested list is " + str(nested_list)

	outlist=[]
	new_list=flatten_list(nested_list)
	print "The flattened list is " + str(new_list)

else:
	inlist = []
	uniq_dict = {}
	l = int(raw_input("Enter the length of the list: "))
	print "Enter the elements of the list"

	for i in range(0,l):
		inlist.append(int(raw_input()))

	print inlist

	for i in inlist:
		if i not in uniq_dict:
			uniq_dict[i] = 1
		else:
			uniq_dict[i] = uniq_dict[i] + 1

	print uniq_dict


