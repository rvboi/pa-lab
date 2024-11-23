# Take a number as input from the user
num = int(input("Enter a number: "))

# Use a for loop to iterate from 1 to 10 and print the multiplication table
print(f"\nMultiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
