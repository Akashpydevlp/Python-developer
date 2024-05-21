# creating an empty list

list = []
 
# number of elements as input

n = int(input("Enter number of elements : "))
 
# iterating till the range

for i in range(0, n):

    ele = int(input())

    # adding the element

    list.append(ele)  
 

print(list)
list.insert(3,6)
print(list)
list.remove(1)
list.append(5)
list.sort()
list.pop(2)
list.reverse()
print(list)
    