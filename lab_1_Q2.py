# Assigning values to variables of different data types
integer_var = 10          # Integer
float_var = 3.14          # Float
string_var = "Hello, "    # String
boolean_var = True        # Boolean

# Perform arithmetic operations on numeric data types
sum_result = integer_var + float_var
product_result = integer_var * float_var

# Concatenate strings using the + operator
greeting = string_var + "world!"

# Use logical operators to evaluate boolean expressions
boolean_and = boolean_var and (integer_var > 5)
boolean_or = boolean_var or (integer_var < 5)

# Print the results with clear formatting
print("Numeric Operations:")
print(f"Sum of {integer_var} and {float_var}: {sum_result}")
print(f"Product of {integer_var} and {float_var}: {product_result}")

print("\nString Operation:")
print(f"Concatenated String: {greeting}")

print("\nBoolean Operations:")
print(f"Boolean AND (True and {integer_var} > 5): {boolean_and}")
print(f"Boolean OR (True or {integer_var} < 5): {boolean_or}")
