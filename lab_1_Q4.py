# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even or odd using the modulus operator
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
