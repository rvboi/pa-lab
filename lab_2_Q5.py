# Take a number as input from the user
num = int(input("Enter a number to find its factorial: "))

# Initialize factorial as 1
factorial = 1

# Calculate factorial using a loop
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0 or num == 1:
    print(f"Factorial of {num} is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
