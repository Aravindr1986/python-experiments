import numpy as np
arr = np.array([1, 2, 3, 4, 5]) # 1D array
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(arr2D)
print(arr3D)
print(f"To get dimension of the array use ndim : {arr2D.ndim}")