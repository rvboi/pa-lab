import numpy as np

# 1D array using np.array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:\n", arr_1d)

# 2D array using np.array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr_2d)
# 3D array using np.array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", arr_3d)
# Array with values ranging from 0 to 9
arr_range = np.arange(10)
print("Array with np.arange:\n", arr_range)
# Array with 10 values equally spaced between 0 and 1
arr_linspace = np.linspace(0, 1, 10)
print("Array with np.linspace:\n", arr_linspace)
