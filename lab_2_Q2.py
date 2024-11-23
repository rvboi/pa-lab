# Create a dictionary to store information about a person
person = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Access values using keys
print("Name:", person['name'])
print("Age:", person['age'])

# Add a new key-value pair to the dictionary
person['email'] = 'john.doe@example.com'
print("\nDictionary after adding email:", person)

# Modify an existing value
person['age'] = 31
print("\nDictionary after modifying age:", person)

# Check if a key exists in the dictionary
if 'city' in person:
    print("\nKey 'city' exists in the dictionary.")

# Get a list of all keys and values
print("\nKeys:", list(person.keys()))
print("Values:", list(person.values()))
