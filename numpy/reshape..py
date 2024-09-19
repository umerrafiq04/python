import numpy as np
# arr=np.array((1,2,3,4,5,6,7,8,9,10))
# arr2=arr.reshape(2,5)
# print(arr.shape)


# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# newarr = arr.reshape(3, 2, 2)

# print(newarr)
'''Unknown Dimension
You are allowed to have one "unknown" dimension.

Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

Pass -1 as the value, and NumPy will calculate this number for you'''
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# newarr = arr.reshape(2, 2, -2)

# print(newarr)

# Flattening array means converting a multidimensional array into a 1D array

arr3= np .array([[1,2,3],[7,8,9]])
print(arr3.ndim)
arr4=arr3.reshape(-1)
print(arr4.ndim)
print(arr4)