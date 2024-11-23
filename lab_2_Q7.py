# Find the sum of all even numbers between 1 and 100
sum_even = sum(i for i in range(1, 101) if i % 2 == 0)

print(f"The sum of all even numbers between 1 and 100 is {sum_even}")
