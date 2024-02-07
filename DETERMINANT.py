#determinant of a 2*2 matrix

def determinant(matrix):
    return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    
list1=list()
list2=list()
print("enter elements of first row")
for i in range(2):
    list1.append(int(input()))
print(list1)
print("enter elements of second row")
for i in range(2):
    list2.append(int(input()))
print(list2)
list3=[list1,list2]
print(list3)
print("Determinant of the 2*2 matrix is :",determinant(list3))