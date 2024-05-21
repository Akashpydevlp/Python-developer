#
'''def maximum(a,b):
    if a>=b:
        return a
    else:
        return b
a=2
b=4
c=maximum(a,b)
print("maximum of",a, "and",b,"is",c)'''
'''
def max3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
        
a=2
b=4
c=9
x=max3(a,b,c)
print("maximum of",a, "and",b,"and",c,"is",x)'''

'''
def max4(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif b>a and b>c and b>d:
        return b
    elif c>a and c>b and c>d:
        return c
    elif d>a and d>b and d>c:
        return d
    
a=10
b=20
c=55
d=99
x=max4(a,b,c,d)
print("maximum of",a, "and",b,"and",c, "and",d,"is",x)'''
'''
Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))
 
# Initialize matrix

matrix = []

print("Enter the entries row wise:")
 
# For user input
# A for loop for row entries

for row in range(Row):    

    a = []

    # A for loop for column entries

    for column in range(Column):   

        a.append(int(input()))

    matrix.append(a)
 
# For printing the matrix

for row in range(Row):

    for column in range(Column):

        print(matrix[row][column], end=" ")

    print()  '''
    
    # creating an empty list

lst = []
 
# number of elements as input

n = int(input("Enter number of elements : "))
 
# iterating till the range

for i in range(0, n):

    ele = int(input())

    # adding the element

    lst.append(ele)
    

print(lst)

print(max(lst))

