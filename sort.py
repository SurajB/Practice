#This is sorting in python

inarr=[]
print("Enter the no of elements to be sorted")
n=int(input())
print(type(n))
print("Enter the elements")
for i in range(0, n):
	m=int(input())
	inarr.append(m)

print("Which sorting techique do you prefer")
print("1.Insertion sort 2.Selection sort 3.Bubble sort \n Enter the option")
option=int(input())

def print_array(array):
	print(array)

#insertion sort
if option==1:
	for i in range(0, n):
		for j in range(0, i):
			if inarr[i] < inarr[j]:
				temp=inarr[i]
				inarr[i]=inarr[j]
				inarr[j]=temp
    #print_array(inarr)

#selection sort
elif option==2:
	temp=inarr[0]
	for i in range(0, n):
		temp=inarr[i]
		swap=i
		for j in range((i+1), n):
			if inarr[j]<temp:
				temp=inarr[j]
				swap=j
		inarr[swap]=inarr[i]
		inarr[i]=temp
	#print_array(inarr)

#Bubble sort
else:
	for i in range(0, n):
		for j in range(0, (n-1)):
			if inarr[j+1]<inarr[j]:
				temp=inarr[j+1]
				inarr[j+1]=inarr[j]
				inarr[j]=temp

print_array(inarr)





