import numpy as np
# 1d array
# arr1=np.array([1,2,3,4,5,6,7,8,0,77,654,6,43,353,4,5,34])
# newarr=np.array_split(arr1,3)
# print(newarr)
# 2d array
# arr3=np.array([[1,2],[3,4],[5,6],[7,8],[9,10]])
# newarr2=np.array_split(arr3,3)
# print(newarr2)
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12],
                [13, 14, 15],
                [16, 17, 18]])

newarr = np.array_split(arr, 3)
newarr2 = np.array_split(arr, 3, axis=1)

print(newarr)
print(newarr2)
