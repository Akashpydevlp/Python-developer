def universal(n):
    
    if n==1:#algebic operation 
        print("ente you choise")
        x=int(input())
        if x==1:#add
            a=int(input())
            b=int(input())
            c=a+b
            print("add",c)
        elif x==2:#sub
            a=int(input())
            b=int(input())
            c=a-b
            print("subtraction",c)
        elif x==3:#multplions 
            a=int(input())
            b=int(input())
            c=a*b
            print("multplions",c)
        elif x==4:#division
            a=int(input())
            b=int(input())
            c=a/b
            print("division",c)  
        elif x==5: # percentage 
            a=int(input())
            b=int(input())
            c=a%b
            print("percentage",c)
        elif x==6:# power 
            a=int(input())
            b=int(input())
            c=a**b
            print("power",c)   
        else:
            print("your choice is worng")
              
            
    elif n==2:#revese string
        x=int(input("Enter your number-------->"))
        y=str(x)
        for i in x:
             y=i+y
    
    
        if(x==y):
             print("yes")
        else:
            print("no")
    elif n==3:
        n=int(input("Enter your number-------->"))
        for i in range(1,n+1):
            n=n*i
            print(n)
    elif n==4:
        n = int(input("Enter the range (n): "))

         # Print even numbers
        print("Even numbers:")
        for i in range(2,n+1,2):
             print(i, end=" ")

         # Print odd numbers
        print("\nOdd numbers:")
        for i in range(1,n+1,2):
            print(i,end=" ")
    
           
    
    elif n==5:
        
        # if the given number is 10
        given_number = int(input("enter your number"))
 
        # set up a variable to store the sum
        # with initial value of 0
        prd = 1
 
         # since we want to include the number 10 in the sum
         # increment given number by 1 in the for loop
        for i in range(1,given_number+1):
            prd*=i
 
        # print the total sum at the end
        print(prd)
universal(5)




    
       
    
           
            
           
    
           



           
        