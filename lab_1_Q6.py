# Create a list of fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Access elements using indexing
print("Original list of fruits:")
print(fruits)
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Modify elements in the list
fruits[1] = "Blueberry"  # Replace "Banana" with "Blueberry"
print("\nList after modifying the second element:")
print(fruits)

# Add elements to the list
fruits.append("Fig")  # Add "Fig" to the end of the list
fruits.insert(2, "Grape")  # Insert "Grape" at the third position
print("\nList after adding elements:")
print(fruits)

# Remove elements from the list
fruits.remove("Date")  # Remove "Date" from the list
popped_fruit = fruits.pop()  # Remove and return the last element
print(f"\nList after removing elements (removed {popped_fruit}):")
print(fruits)

# Find the length of the list
length_of_list = len(fruits)
print(f"\nLength of the list: {length_of_list}")

# Sort the list in ascending order
fruits.sort()
print("\nList sorted in ascending order:")
print(fruits)

# Sort the list in descending order
fruits.sort(reverse=True)
print("\nList sorted in descending order:")
print(fruits)
