# Create a tuple of colors
colors = ('red', 'green', 'blue', 'yellow', 'red')

# Access elements using indexing
print("First color:", colors[0])
print("Last color:", colors[-1])

# Try to modify an element in the tuple (This will raise an error)
try:
    colors[1] = 'purple'
except TypeError as e:
    print("\nError: Cannot modify a tuple element (Tuples are immutable).")

# Find the number of occurrences of a specific element (e.g., 'red')
count_red = colors.count('red')
print("\nNumber of occurrences of 'red':", count_red)
