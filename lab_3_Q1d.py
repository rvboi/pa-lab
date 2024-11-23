import numpy as np
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
# Reshape example
reshaped = arr_1d.reshape(5, 1)
print("Reshaped 1D array:\n", reshaped)

# Resize modifies the shape in-place
arr_resized = np.resize(arr_1d, (3, 2))
print("Resized array (3x2):\n", arr_resized)

# Flatten example
flat_array = arr_2d.flatten()
print("Flattened 2D array:\n", flat_array)
