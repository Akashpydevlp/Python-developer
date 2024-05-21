n1=int(input("enter the value of num1-->"))
length=len(n1)

if length!=3:
    print("3 digit num")
else:
    print("middle digit is", (int(n1)%100//10))

