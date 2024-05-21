a=[12,67,89,66,88]

for x in a:
    print(x)
    
a.clear()
print(a)
a=[1,2,3,4,5,6,7,9]
for i in range((len(a))):
    print(a[i])
    
    
a=[10,2,3,8,5,6,7,8,3]
a.sort(reverse=False)
print(a)


b=a.copy()
print(b)

c=a+b
print(c)

a=[1,2,3,4,5,6,7,8]
a[7]=9
a[-1]=9
print(a)

a=[1,2,3,4,5,6,7,8,]
a[1]=9
a[2]=8
print(a)



a=[1,2,3,4,5,6]
print(a)
print(type(a))


a=[1,2,3,4,5]
 
a[2]=6
print(a)

a=1
b=4
c=5+2j
print(a+b+c)
a=[1,2,3,4,5,6,7]
c=max(a)
g=min(a)
print(c,g)

print(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6],(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6])/7)

a=True
print(a)


x=8&3+4
print(x)

x=8&3|4
print(x)

y=7|3*4+7
print(y)

n=4
if(n%2==0):
    print("Even")
else:
    print("Even")
   
A=39
if  80<a<=90:
    print("A")
elif  70<a<=80:
    print("B")
elif 60<a<=70:
    print("c")
elif 50<a<=60:
    print("D")
elif 40<a<=50:
    print("pass")
else:
    print("fail")
    