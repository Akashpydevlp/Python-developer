a=[1,2,3,4,5,6]
print(a)
print(type(a))

a=[1,1,2]
print(a)
print(type(a))

a=[1,2,"a",2.3,True,1+3j]
print(a)
print(type(a))

print(a[-5])

a=[1,2,3,4,5]
 
a[2]=9

print(a)

a=[2,3]
a[0]=3
a[1]=2

print(a)

a=[1,2,3,4,5,6,7,8,9]

print(a[1:7])
print(a)


a=[1,2,3,4,5,6,7,8,9]


if 0 in a:
    print("yes")
    
else:
    print("no")
    
a.insert(3,0)
print(a)

a.append(88)
print(a)

a=[2,4,6]
b=[3,5,7]

a.extend(b)
print(a)

a=[2,6,7,8,9]

a.remove(7)
print(a)

del a[3]

del a
print(a)


    
