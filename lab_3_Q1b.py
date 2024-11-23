import numpy as np
# Indexing example
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_range = np.arange(10)
print("Element at index 2 in 1D array:", arr_1d[2])

# Slicing example
print("Slice from index 1 to 3 in 2D array:\n", arr_2d[:, 1:3])
# Reshaping array into different dimensions
reshaped_array = arr_range.reshape(2, 5)
print("Reshaped array (2x5):\n", reshaped_array)
# Concatenate two arrays
concatenated_array = np.concatenate((arr_1d, np.array([6, 7, 8])))
print("Concatenated array:\n", concatenated_array)
