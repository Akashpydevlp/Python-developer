def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Prompt the user to enter a positive integer
number = int(input("Enter a positive integer: "))

# Check if the number is negative
if number < 0:
    print("Error! Factorial of a negative number doesn't exist.")
else:
    # Calculate the factorial of the number
    result = factorial(number)
    print(f"Factorial of {number} = {result}")