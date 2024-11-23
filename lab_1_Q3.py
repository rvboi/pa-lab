# Prompt the user to enter their name
name = input("Enter your name: ")

# Greet the user
print(f"Hello, {name}!")

# Prompt the user to enter their birth year
birth_year = int(input("Enter your birth year: "))

# Calculate the current year
from datetime import datetime
current_year = datetime.now().year

# Calculate the user's age
age = current_year - birth_year

# Display the user's age
print(f"{name}, you are {age} years old.")
