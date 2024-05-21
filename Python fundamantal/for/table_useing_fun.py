'''print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")


#looping 

for x in range(2,40,7):
    if x==7:
        break
print(x)

a=int(input("enter your number--->"))
n=int(input("enter the number---->"))
for x in range(1,n+1):
    table=x*a
    print(table)'''



def table(a,n):
    for x in range(1,n+1):
         table=x*a
         print(table)
        
    
x=table(3,10)




