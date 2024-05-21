print("&________welcome______&")
print("Inter your choice.....")
print("1st.+ Add")
print("2nd.- Subtraction")
print("3rd.* Multplaction")
print("4th./ divison")
print("5th.& modular operator")
print("6th.//flow divison")
print("7.** power function")
print("8.% percentage")




x=int(input("Enter your Number"))
if x==1: #add
  a=int(input("a==>"))
  b=int(input("b==>"))
  print(a+b)
elif x==2:#subtaction
  a=int(input("a==>"))
  b=int(input("b==>"))
  print(a-b)
elif x==3: #mutli
  a=int(input("a==>"))
  b=int(input("b==>"))
  print(a*b)
elif x==4: # divison
  a=int(input("a==>"))
  b=int(input("b==>"))
  print(a/b)  
elif x==5: # modular operator
  a=int(input("a==>"))
  b=int(input("b==>"))
  print(a%b) 
elif x==6: # flow divison
  a=int(input("a==>"))
  b=int(input("b==>"))
  print(a//b)   
elif x==7: # power function
  print("Your choice is power fuction7")

  a=int(input("a==>"))
  b=int(input("power"))
  y=a**b
  print("Your Answer==>",y) 
  
elif x==8: # percentage
  print("Your choice is Percentage")
  a=int(input("Out come==>"))
  b=int(input("Total==>"))
  p=(a/b)*100
  print(a%b) 
  
  
    
    
