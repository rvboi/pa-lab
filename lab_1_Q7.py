# Create a string variable
my_string = "My name is Rahul Verma"

# Find the length of the string
string_length = len(my_string)
print(f"Length of the string: {string_length}")

# Convert the string to uppercase
uppercase_string = my_string.upper()
print(f"Uppercase: {uppercase_string}")

# Convert the string to lowercase
lowercase_string = my_string.lower()
print(f"Lowercase: {lowercase_string}")

# Check if a substring exists in the string
substring = "Python"
is_substring_present = substring in my_string
print(f"Is '{substring}' present in the string? {is_substring_present}")

# Split the string into a list of words
words_list = my_string.split()
print(f"List of words: {words_list}")
