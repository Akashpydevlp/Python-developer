# Get the range from the user
n = int(input("Enter the range (n): "))

# Print even numbers
print("Even numbers:")
for i in range(2, n+1, 2):
    print(i, end=" ")

# Print odd numbers
print("\nOdd numbers:")
for i in range(1, n+1, 2):
    print(i, end=" ")
    