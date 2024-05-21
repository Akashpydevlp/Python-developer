n=int(input("inter your number----->"))
if  (n%2!=10):
    print("weird")
elif(n%2==0)&(2<=n<=5):
    print("Not weird")
elif (n%2==0)&(6<=n<=20):
      print("weird")
elif (n%2==0)&(20<=n):
     print("Not weird")
else:
     print("Out of Scope value")
      