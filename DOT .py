#DOT product of two vectors
list1=list()
list2=list()
n=int(input("enter number of dimensions"))
print("enter your 1st VECTOR elements")
for i in range(n):
	list1.append(int(input()))
print(list1)
print("enter your 2nd VECTOR elements")
for i in range(n):
	list2.append(int(input()))
print(list2)
sum=0
for i in range(n):
	sum+=(list1[i]*list2[i])
print("DOT PRODUCT IS :",sum)
