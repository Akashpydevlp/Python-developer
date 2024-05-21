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



